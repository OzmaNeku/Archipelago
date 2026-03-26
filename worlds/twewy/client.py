from typing import TYPE_CHECKING, Set, Optional, List, Tuple
from NetUtils import ClientStatus
import asyncio
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .items import ITEM_TO_LOCATION
from .locations import LOCATION_TO_ITEM
from .items import STACKABLE_ITEM_TO_LOCATION


if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext



# Constants for memory layout
INVENTORY_BASE = 0x02072C80
INVENTORY_SIZE = 1120
SLOT_SIZE = 4
OVIS_CANTUS_KILL_FLAG = 0x02073E44
RAM_DOMAIN = "ARM9 System Bus"


class TWEWYClient(BizHawkClient):
    game = "The World Ends With You"
    system = "NDS"
    patch_suffix = ".aptwewy"

    local_checked_locations: Set[int]
    ram_mem_domain = RAM_DOMAIN
    inventory_base = INVENTORY_BASE
    ovis_cantus_kill_flag = OVIS_CANTUS_KILL_FLAG

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = {}
        self.received_items_count = 0
        self.injected_items = {}
        self.goal_complete = False

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 1
        return True

    async def _parse_inventory(self, data: bytes) -> dict:
        items = {}
        for i in range(0, INVENTORY_SIZE, SLOT_SIZE):
            low = data[i]
            if low != 0xFF:
                high = data[i + 1]
                qty = data[i + 2]
                idx = low + (high << 8)
                items[idx] = qty
        return items

    async def _remove_pickup_slot(self, ctx: "BizHawkClientContext", offset: int) -> None:
        addr = self.inventory_base + offset
        await bizhawk.write(
            ctx.bizhawk_ctx,
            [(addr, bytes([0xFF, 0xFF, 0x00, 0x00]), self.ram_mem_domain)],
        )

    async def _increase_slot_quantity(self, ctx: "BizHawkClientContext", offset: int, current_qty: int) -> None:
        addr = self.inventory_base + offset + 2
        await bizhawk.write(
            ctx.bizhawk_ctx,
            [(addr, bytes([current_qty + 1]), self.ram_mem_domain)],
        )

    async def _write_new_item_slot(self, ctx: "BizHawkClientContext", offset: int, combined_index: int) -> None:
        addr = self.inventory_base + offset
        low_byte = combined_index & 0xFF
        high_byte = (combined_index >> 8) & 0xFF
        await bizhawk.write(
            ctx.bizhawk_ctx,
            [(addr, bytes([low_byte, high_byte, 0x01, 0x00]), self.ram_mem_domain)],
        )

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        try:
            if ctx.slot_data is None:
                return

            # Re-read inventory before injecting to get fresh state
            read_state = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                    (self.inventory_base, INVENTORY_SIZE, self.ram_mem_domain),
                    (self.ovis_cantus_kill_flag, 4, self.ram_mem_domain),
                ],
            )
            
            inventory_data = read_state[0]
            kill_flag_data = read_state[1]

            current_items = await self._parse_inventory(inventory_data)

            if ctx.slot_data.get("start_with_phone_menu") and 0x2A7 not in current_items and 0x2A7 not in self.injected_items:
                for i in range(0, INVENTORY_SIZE, SLOT_SIZE):
                    if inventory_data[i] == 0xFF:
                        await self._write_new_item_slot(ctx, i, 0x2A7)
                        self.injected_items[0x2A7] = self.injected_items.get(0x2A7, 0) + 1
                        break

            if kill_flag_data[0] == 1 and not self.goal_complete:
                self.goal_complete = True
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

            new_items = set()
            locations_to_check = []

            # Detect new items
            for idx in current_items:
                injected_qty = self.injected_items.get(idx, 0)
                prev_qty = self.local_checked_locations.get(idx, 0)
                current_qty = current_items[idx]
                natural_qty = current_qty - injected_qty
                if natural_qty > prev_qty:
                    if idx in ITEM_TO_LOCATION and prev_qty == 0:
                        new_items.add(idx)
                        locations_to_check.append(ITEM_TO_LOCATION[idx])

            # Add item to its stack
            for idx, qty in current_items.items():
                if idx in self.injected_items:
                    continue
                prev_qty = self.local_checked_locations.get(idx, 0)
                if qty > prev_qty:
                    for grant in range(prev_qty + 1, qty + 1):
                        if (idx, grant) in STACKABLE_ITEM_TO_LOCATION:
                            locations_to_check.append(STACKABLE_ITEM_TO_LOCATION[(idx, grant)])

            # Remove items on pickup
            for item_idx in new_items:
                if item_idx not in ITEM_TO_LOCATION:
                    continue
                for i in range(0, INVENTORY_SIZE, SLOT_SIZE):
                    low = inventory_data[i]
                    high = inventory_data[i + 1]
                    if (low + (high << 8)) == item_idx:
                        await self._remove_pickup_slot(ctx, i)
                        break

            if locations_to_check:
                await ctx.send_msgs([{"cmd": "LocationChecks", "locations": locations_to_check}])

            for index, network_item in enumerate(ctx.items_received[self.received_items_count:], start=self.received_items_count):
                combined_index = LOCATION_TO_ITEM.get(network_item.item)
                if combined_index is None:
                    continue

                # Fresh read for each injection
                fresh_read = await bizhawk.read(
                    ctx.bizhawk_ctx,
                    [(self.inventory_base, INVENTORY_SIZE, self.ram_mem_domain)],
                )
                fresh_inventory = fresh_read[0]

                item_found = False
                for i in range(0, INVENTORY_SIZE, SLOT_SIZE):
                    low = fresh_inventory[i]
                    high = fresh_inventory[i + 1]
                    if (low + (high << 8)) == combined_index:
                        current_qty = fresh_inventory[i + 2]
                        await self._increase_slot_quantity(ctx, i, current_qty)
                        item_found = True
                        break

                if not item_found:
                    for i in range(0, INVENTORY_SIZE, SLOT_SIZE):
                        if fresh_inventory[i] == 0xFF:
                            await self._write_new_item_slot(ctx, i, combined_index)
                            break

                self.injected_items[combined_index] = self.injected_items.get(combined_index, 0) + 1
                self.received_items_count = index + 1

            self.local_checked_locations = current_items
        except (bizhawk.RequestFailedError, bizhawk.ConnectorError):
            pass