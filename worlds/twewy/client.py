from typing import TYPE_CHECKING, Set
from NetUtils import ClientStatus
import asyncio
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

ITEM_TO_LOCATION = {
    0x2A7: 0xC0DE0000,  # Phone Menu
    0x2DB: 0xC0DE0001,  # Wearing Pins
}

class TWEWYClient(BizHawkClient):
    game = "The World Ends With You"
    system = "NDS"
    patch_suffix = ".aptwewy"

    local_checked_locations: Set[int]

    ram_mem_domain = "ARM9 System Bus"
    inventory_base = 0x02072C80

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 1
        return True
    
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        
        try:
            read_state = await bizhawk.read(
                ctx.bizhawk_ctx, [
                    (self.inventory_base, 1120, self.ram_mem_domain)
                ]
            )
            current_items = set()
            for i in range(0, 1120, 4):
                if read_state[0][i] != 0xFF:
                    idx = read_state[0][i] + (read_state[0][i+1]*0x100)
                    current_items.add(idx)

            new_items = current_items - self.local_checked_locations
            if new_items:
                locations_to_check = [ITEM_TO_LOCATION[i] for i in new_items if i in ITEM_TO_LOCATION]
                if locations_to_check:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": locations_to_check}])
            self.local_checked_locations = current_items
        except bizhawk.RequestFailedError:
            pass
        except bizhawk.ConnectorError:
            pass
