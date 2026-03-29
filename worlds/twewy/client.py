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
location_base = 0x020746E0
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
    location_base = location_base
    ovis_cantus_kill_flag = ovis_cantus_kill_flag


    def __init__(self) -> None:
        super().__init__()
        self.checks_seen = set()
        self.server_items = 0
        self.goal_complete = False
        self.item_grant_counts = {}
        self.injected_items = {}
        self.phone_sent = False

    # Check if ROM is working as intended and keep inventory up to date
    async def validate_rom(self, context: "BizHawkClientContext") -> bool:
        print("Validate Rom called")
        context.game = self.game
        context.items_handling = 0b111
        context.want_slot_data = True
        context.watcher_timeout = 1
        # Initialize location buffer to FF so Lua script can find empty slots
        buffer = bytes([0xFF, 0xFF, 0x00, 0x00] * 280)
        await bizhawk.write(context.bizhawk_ctx, [
            (location_base, buffer, ram_domain)
        ])
        return True

    # Begin game watcher
    async def game_watcher(self, context: "BizHawkClientContext") -> None:
        from CommonClient import logger

        try:
            # If slot data is none, return.
            if context.slot_data is None:
                return

            # 1. Inject items received from server directly into inventory
            # The Lua script at 0x02022D78 only intercepts natural game writes,
            # so direct inventory writes will never appear in the location buffer
            for index, network_item in enumerate(context.items_received[self.server_items:], start=self.server_items):
                edited = False
                combined_index = LOCATION_TO_ITEM.get(network_item.item)
                if combined_index is None:
                    self.server_items = index + 1
                    continue

                # 1.1 Get fresh read from inventory
                fresh_read = await bizhawk.read(
                    context.bizhawk_ctx, [
                        (self.inventory_base, inventory_size, self.ram_mem_domain),
                    ]
                )
                fresh_inventory_data = fresh_read[0]

                # 1.2 If item already exists, increment using archipelago count
                for i in range(0, inventory_size, 4):
                    if fresh_inventory_data[i] != combined_index & 0xFF:
                        continue
                    if fresh_inventory_data[i + 1] != (combined_index >> 8) & 0xFF:
                        continue
                    new_qty = self.injected_items.get(combined_index, 0) + 1
                    logger.info("Sending item to inventory FROM SERVER, iterating version")
                    await bizhawk.write(
                        context.bizhawk_ctx, [
                            (inventory_base + i, bytes([combined_index & 0xFF, (combined_index >> 8) & 0xFF, new_qty, 0x00]), ram_domain)
                        ])
                    self.injected_items[combined_index] = new_qty
                    edited = True
                    break



                if not edited:
                    # 1.3 If item doesn't exist, write it to a new empty slot
                    for i in range(0, inventory_size, 4):
                        if fresh_inventory_data[i] != 0xFF:
                            continue
                        logger.info("Sending item to inventory FROM SERVER, single version.")
                        await bizhawk.write(
                            context.bizhawk_ctx, [
                                (inventory_base + i, bytes([combined_index & 0xFF, (combined_index >> 8) & 0xFF, 0x01, 0x00]), ram_domain)
                            ]
                        )
                        self.injected_items[combined_index] = self.injected_items.get(combined_index, 0) + 1
                        break

                self.server_items = index + 1
                break  # Only inject one item per frame

            # 2. Read location buffer, inventory and kill flag
            # Location buffer is written to by the Lua script when the game
            # naturally grants an item at 0x02022D78
            read_state = await bizhawk.read(
                context.bizhawk_ctx, [
                    (self.location_base, inventory_size, self.ram_mem_domain),
                    (self.inventory_base, inventory_size, self.ram_mem_domain),
                    (self.ovis_cantus_kill_flag, 4, self.ram_mem_domain),
                ]
            )
            location_data = read_state[0]
            inventory_data = read_state[1]
            boss_kill_data = read_state[2]

            # 3. Options checks

            # 3.1 Phone menu option - inject directly, bypasses Lua intercept
            if context.slot_data.get("start_with_phone_menu") and not self.phone_sent:
                for i in range(0, inventory_size, 4):
                    if inventory_data[i] == 0xFF:
                        await bizhawk.write(context.bizhawk_ctx, [
                            (inventory_base + i, bytes([0xA7, 0x02, 0x01, 0x00]), ram_domain)
                        ])
                        self.injected_items[0x2A7] = self.injected_items.get(0x2A7, 0) + 1
                        break
                self.phone_sent = True
                logger.info("Sent phone menu")

            # 3.2 Text skip - continuously write or will be purged on phone menu open
            if context.slot_data.get("start_with_text_skip"):
                await bizhawk.write(context.bizhawk_ctx, [
                    (0x020B0478, bytes([0x01, 0x00, 0xA0, 0xE3]), ram_domain)
                ])

            # 4. Parse location buffer into check_items
            # Only natural pickups intercepted by Lua appear here
            check_items = {}
            for i in range(0, inventory_size, 4):
                if location_data[i] == 0xFF:
                    continue
                idx = location_data[i] + (location_data[i+1] << 8)
                check_items[idx] = location_data[i+2]
                logger.info(f"check_items: idx={hex(idx)} byte0={location_data[i]:02X} byte1={location_data[i+1]:02X} byte2={location_data[i+2]:02X} byte3={location_data[i+3]:02X}")

            # 5. Build locations to check for unique items
            new_items = {idx: qty for idx, qty in check_items.items() if idx not in self.checks_seen}
            locations_to_check = [ITEM_TO_LOCATION[i] for i in new_items if i in ITEM_TO_LOCATION]

            # 6. Build locations to check for stackable items
            for idx in [0x2A8, 0x2B3, 0x2B2]:
                if idx not in check_items:
                    continue
                next_grant = self.item_grant_counts.get(idx, 0) + 1
                if (idx, next_grant) in ITEM_GRANT_TO_LOCATION:
                    locations_to_check.append(ITEM_GRANT_TO_LOCATION[(idx, next_grant)])
                self.item_grant_counts[idx] = next_grant

            # 7. Send location checks to server
            if locations_to_check:
                logger.info(f"Sending checks: {[hex(l) for l in locations_to_check]}")
                await context.send_msgs([{"cmd": "LocationChecks", "locations": locations_to_check}])
                self.checks_seen.update(new_items)

            # 8. Clear location buffer after reading so it's ready for next pickup
            for i in range(0, inventory_size, 4):
                if location_data[i] != 0xFF:
                    await bizhawk.write(
                        context.bizhawk_ctx, [
                            (location_base + i, bytes([0xFF, 0xFF, 0x00, 0x00]), ram_domain)
                        ]
                    )

            # 9. Clear naturally picked up items from inventory
            # If item was previously injected, just decrement the injected count
            # and leave the slot alone — player already has it from injection
            # If item was not injected, clear the slot entirely
            for i in range(0, inventory_size, 4):
                if inventory_data[i] == 0xFF:
                    continue
                idx = inventory_data[i] + (inventory_data[i+1] << 8)
                if idx in check_items and (idx in ITEM_TO_LOCATION or idx in [0x2A8, 0x2B3, 0x2B2]):
                    logger.info(f"inventory slot: idx={hex(idx)} byte0={inventory_data[i]:02X} byte1={inventory_data[i+1]:02X} byte2={inventory_data[i+2]:02X} byte3={inventory_data[i+3]:02X}")
                    if self.injected_items.get(idx, 0) > 0:
                        self.injected_items[idx] -= 1
                        actual_qty = inventory_data[i+2] - 0x10
                        if actual_qty > 1:
                            await bizhawk.write(
                                context.bizhawk_ctx, [
                                    (inventory_base + i + 2, bytes([actual_qty - 1 + 0x10]), ram_domain)
                                ]
                            )
                        else:
                            await bizhawk.write(
                                context.bizhawk_ctx, [
                                    (inventory_base + i, bytes([0xFF, 0xFF, 0x00, 0x00]), ram_domain)
                                ]
                            )
                    else:
                        # Item was not injected — clear the slot entirely
                        await bizhawk.write(
                            context.bizhawk_ctx, [
                                (inventory_base + i, bytes([0xFF, 0xFF, 0x00, 0x00]), ram_domain)
                            ]
                        )

            # 10. Goal check
            if boss_kill_data[0] == 1 and not self.goal_complete:
                self.goal_complete = True
                await context.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

        except (bizhawk.RequestFailedError, bizhawk.ConnectorError):
            pass