from typing import TYPE_CHECKING, Optional
from NetUtils import ClientStatus
import asyncio
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from CommonClient import logger

from .items import ITEM_TO_LOCATION
from .locations import LOCATION_TO_ITEM

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
    patch_suffix = ".aptwewy"

    # Ram and inventory and kill flag basis
    ram_mem_domain = ram_domain
    inventory_base = inventory_base
    ovis_cantus_kill_flag = ovis_cantus_kill_flag


    def __init__(self):
        super().__init__()
        self.checks_seen = set()
        self.server_items = 0
        self.goal_complete = False

    # Check if ROM is working as intended and keep inventory up to date
    async def validate_rom(self, context: "BizHawkClientContext") -> bool:
        context.game = self.game
        context.items_handling = 0b111
        context.want_slot_data = True
        context.watcher_timeout = 1
        return True
    
    # Begin game watcher
    async def game_watcher(self, context: "BizHawkClientContext") -> None:
        # Logger line for troubleshooting
        from CommonClient import logger

        try:
            # If slot data is none, restart the try.
            if context.slot_data is None:
                return
            
            #Check inventory and kill flag.
            read_state = await bizhawk.read(
                context.bizhawk_ctx, [
                    (self.inventory_base, inventory_size, self.ram_mem_domain),
                    (self.ovis_cantus_kill_flag, 4, self.ram_mem_domain),
                ]
            )

            # Data from read state
            inventory_data = read_state[0]
            boss_kill_data = read_state[1]

            current_items = set()
            for i in range(0, inventory_size, 4):
                # If the item is 0xFF, skip. It's empty.
                if inventory_data[i] == 0xFF:
                    continue
                # Add the data to the current item pool.
                current_items.add(inventory_data[i] + (inventory_data[i+1] << 8))

            # New items we have
            new_items = current_items - self.checks_seen

            # create array with locations that exist
            locations_to_check = [ITEM_TO_LOCATION[i] for i in new_items if i in ITEM_TO_LOCATION]

            # If locations exist, send them.
            if locations_to_check:
                await context.send_msgs([{"cmd": "LocationChecks", "locations": locations_to_check}])
                self.checks_seen.update(new_items)

            # Clear item from inventory if location was the last check.
            for i in range(0, inventory_size, 4):
                if inventory_data[i] == 0xFF:
                    continue
                idx = inventory_data[i] + (inventory_data[i+1] << 8)
                if idx in new_items and idx in ITEM_TO_LOCATION:
                    await bizhawk.write(
                        context.bizhawk_ctx, [
                            (inventory_base + i, bytes([0xFF, 0xFF, 0x00, 0x00]), ram_domain)
                        ]
                    )

            # Injecting into the game itself from other games.
            for index, network_item in enumerate(context.items_received[self.server_items:], start=self.server_items):
                combined_index = LOCATION_TO_ITEM.get(network_item.item)
                if combined_index is None:
                    continue
                read_state = await bizhawk.read(
                    context.bizhawk_ctx, [
                        (self.inventory_base, inventory_size, self.ram_mem_domain),
                    ]
                )
                
                # Grab fresh inventory data
                fresh_inventory_data = read_state[0]

                #Loop through and write to empty slot
                for i in range(0, inventory_size, 4):
                    if fresh_inventory_data[i] != 0xFF:
                        continue
                    await bizhawk.write(
                        context.bizhawk_ctx, [
                            (inventory_base + i, bytes([combined_index & 0xFF, (combined_index >> 8) & 0xFF, 0x01, 0x00]), ram_domain)
                        ]
                    )
                    break

                # Check up on server items.
                self.server_items = index + 1

            # Check to see if boss is dead
            if boss_kill_data[0] == 1 and not self.goal_complete:
                self.goal_complete = True
                await context.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

        # Exception pass.
        except bizhawk.RequestFailedError:
            pass
        except bizhawk.ConnectorError:
            pass

       