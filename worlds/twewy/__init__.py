from worlds.AutoWorld import World
from Options import Toggle, PerGameCommonOptions
from dataclasses import dataclass

from .items import item_name_to_id, item_classifications
from .locations import location_name_to_id

from BaseClasses import Region, Location, Item, ItemClassification

class StartWithPhoneMenu(Toggle):
    """Start the game with the cell phone unlocked."""
    display_name = "Start with Phone Menu"


@dataclass
class TWEWYOptions(PerGameCommonOptions):
    start_with_phone_menu: StartWithPhoneMenu

class TWEWYWorld(World):
    game = "The World Ends With You"
    topology_present = False

    options_dataclass = TWEWYOptions
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def create_regions(self):
        region = Region("Menu", self.player, self.multiworld)
        for i in self.location_name_to_id:
            location = Location(self.player, i, self.location_name_to_id[i], region)
            region.locations.append(location)
        self.multiworld.regions.append(region)

    def create_items(self):
        for name, id in self.item_name_to_id.items():
            classification = item_classifications.get(name, ItemClassification.filler)
            item = Item(name, classification, id, self.player)
            self.multiworld.itempool.append(item)

    def get_filler_item_name(self) -> str:
        return "(S) Phone Menu"
    
    def fill_slot_data(self):
        return {
            "start_with_phone_menu": self.options.start_with_phone_menu.value,
        }


try:
    from .client import TWEWYClient
    print(f"TWEWYClient loaded successfully")
except Exception as e:
    import traceback
    print(f"Failed to load client: {e}")
    traceback.print_exc()
