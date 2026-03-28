from typing import TYPE_CHECKING, Optional
from NetUtils import ClientStatus
import asyncio
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .locations import LOCATION_TO_ITEM
from .items import ITEM_TO_LOCATION, ITEM_GRANT_TO_LOCATION


if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

# Constants for memory layout
inventory_base = 0x02072C80
inventory_size = 1120
byte_size = 4
ovis_cantus_kill_flag = 0x02073E44
ram_domain = "ARM9 System Bus"



class TWEWYClient(BizHawkClient):
    # Game info
    game = "The World Ends With You"
    system = "NDS"

    # Ram and inventory and kill flag basis
    ram_mem_domain = ram_domain
    inventory_base = inventory_base
    ovis_cantus_kill_flag = ovis_cantus_kill_flag


    def __init__(self) -> None:
        super().__init__()
        self.checks_seen = set()
        self.server_items = 0
        self.goal_complete = False
        self.item_grant_counts = {}
        self.injected_items = {}
        self.previous_items = set()
        self.phone_sent = False
        self.text_skip_sent = False

    # Check if ROM is working as intended and keep inventory up to date
    async def validate_rom(self, context: "BizHawkClientContext") -> bool:
        print("Validate Rom called")
        context.game = self.game
        context.items_handling = 0b111
        context.want_slot_data = True
        context.watcher_timeout = 1
        return True

    # Begin game watcher
    async def game_watcher(self, context: "BizHawkClientContext") -> None:
        from CommonClient import logger

        try:
            # If slot data is none, return.
            if context.slot_data is None:
                return

            # 1. Inject items received from server
            for index, network_item in enumerate(context.items_received[self.server_items:], start=self.server_items):
                combined_index = LOCATION_TO_ITEM.get(network_item.item)
                if combined_index is None:
                    continue

                # 1.1 Get fresh read from the inventory
                fresh_read = await bizhawk.read(
                    context.bizhawk_ctx, [
                        (self.inventory_base, inventory_size, self.ram_mem_domain),
                    ]
                )
                fresh_inventory_data = fresh_read[0]


                # 1.2 if item exists, iterate
                edited = False
                for i in range(0, inventory_size, 4):
                    if fresh_inventory_data[i] != combined_index & 0xFF:
                        continue

                    #if fresh_inventory_data[i + 2] == self.injected_items[combined_index & 0xFF]:
                        #edited = True
                        #logger.info("We break here:" + str(fresh_inventory_data[i+2]))
                        #break
                                   
                    logger.info((fresh_inventory_data[i + 2] + 1))
                    await bizhawk.write(
                        context.bizhawk_ctx, [
                            (inventory_base + i, bytes([combined_index & 0xFF, (combined_index >> 8) & 0xFF, (fresh_inventory_data[i + 2] + 1), 0x00]), ram_domain)
                        ])
                    self.injected_items[combined_index & 0xFF] = fresh_inventory_data[i + 2] + 1
                    edited = True
                    break

                if edited == True:
                    continue

                for i in range(0, inventory_size, 4):
                    if fresh_inventory_data[i] != 0xFF:
                        continue
                    await bizhawk.write(
                        context.bizhawk_ctx, [
                            (inventory_base + i, bytes([combined_index & 0xFF, (combined_index >> 8) & 0xFF, 0x01, 0x00]), ram_domain)
                        ]
                    )
                    self.injected_items[combined_index & 0xFF] = 1
                    break

                self.server_items = index + 1

            # 2. Read current inventory and kill flag after injection
            read_state = await bizhawk.read(
                context.bizhawk_ctx, [
                    (self.inventory_base, inventory_size, self.ram_mem_domain),
                    (self.ovis_cantus_kill_flag, 4, self.ram_mem_domain),
                ]
            )
            inventory_data = read_state[0]
            boss_kill_data = read_state[1]

            # 3. Parse inventory into current_items
            current_items = {}
            for i in range(0, inventory_size, 4):
                if inventory_data[i] == 0xFF:
                    continue
                idx = inventory_data[i] + (inventory_data[i+1] << 8)
                current_items[idx] = inventory_data[i+2]

            # 4.Options checks

            # 4.1 - Phone menu
            if context.slot_data.get("start_with_phone_menu") and 0x2A7 not in current_items and 0x2A7 not in self.injected_items and self.phone_sent == False:
                for i in range(0, inventory_size, 4):
                    if inventory_data[i] == 0xFF:
                        await bizhawk.write(context.bizhawk_ctx, [
                            (inventory_base + i, bytes([0xA7, 0x02, 0x01, 0x00]), ram_domain)
                        ])
                        self.injected_items[0x2A7] = self.injected_items.get(0x2A7, 0) + 1
                        break
                self.phone_sent = True
                logger.info("Sent phone menu")

            # 4.2 - Text skip - has to continously write or will be purged on phone menu open
            if context.slot_data.get("start_with_text_skip"):
                await bizhawk.write(
                    context.bizhawk_ctx, [
                        (0x020B0478, bytes([0x01, 0x00, 0xA0, 0xE3]), ram_domain)
                    ]  
                )

            # 5. New items we have
            new_items = {idx: qty for idx, qty in current_items.items() 
             if idx not in self.checks_seen 
             and qty > self.injected_items.get(idx, 0)}

            # 6. Build locations to check for unique items
            locations_to_check = [ITEM_TO_LOCATION[i] for i in new_items if i in ITEM_TO_LOCATION]

            # 7. Build locations to check for stackable items
            for idx in [0x2A8, 0x2B3, 0x2B2]:
                if idx not in current_items:
                    continue
                if idx in self.previous_items:
                    continue
                if self.injected_items.get(idx, 0) > 0:
                    continue
                next_grant = self.item_grant_counts.get(idx, 0) + 1
                if (idx, next_grant) in ITEM_GRANT_TO_LOCATION:
                    locations_to_check.append(ITEM_GRANT_TO_LOCATION[(idx, next_grant)])
                self.item_grant_counts[idx] = next_grant

            # 8. Send location checks
            if locations_to_check:
                await context.send_msgs([{"cmd": "LocationChecks", "locations": locations_to_check}])
                self.checks_seen.update(new_items)

            # 9. Clear naturally picked up items from inventory
            for i in range(0, inventory_size, 4):
                if inventory_data[i] == 0xFF:
                    continue
                idx = inventory_data[i] + (inventory_data[i+1] << 8)
                if idx in new_items and idx in ITEM_TO_LOCATION:
                    if self.injected_items.get(idx, 0) > 0:
                        # 9.1 Item was previously injected, just decrement injected count
                        self.injected_items[idx] -= 1
                    else:
                        # 9.2 Item did not exist before, clear the slot entirely
                        await bizhawk.write(
                            context.bizhawk_ctx, [
                                (inventory_base + i, bytes([0xFF, 0xFF, 0x00, 0x00]), ram_domain)
                            ]
                        )

            # 10. Goal check
            if boss_kill_data[0] == 1 and not self.goal_complete:
                self.goal_complete = True
                await context.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

            self.previous_items = set(current_items.keys())

        except (bizhawk.RequestFailedError, bizhawk.ConnectorError):
            pass