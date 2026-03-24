from worlds.AutoWorld import World

from BaseClasses import Region, Location, Item, ItemClassification

ITEM_TO_LOCATION = {
    0x2A7: 0xC0DE0000,  # Phone Menu
    0x2DB: 0xC0DE0001,  # Wearing Pins
}

class TWEWYWorld(World):
    game = "The World Ends With You"
    topology_present = False
    item_name_to_id = {
        "(S) Phone Menu": 0xC0DE0000,
        "(B) Wearing Pins": 0xC0DE0001,
    }
    location_name_to_id = {
        "Phone Menu": 0xC0DE0000,
        "Wearing Pins": 0xC0DE0001,
    }

    def create_regions(self):
        region = Region("Menu", self.player, self.multiworld)
        for i in self.location_name_to_id:
            location = Location(self.player, i, self.location_name_to_id[i], region)
            region.locations.append(location)
        self.multiworld.regions.append(region)

    def create_items(self):
        for i in self.item_name_to_id:
            item = Item(i, ItemClassification.filler, self.item_name_to_id[i], self.player)
            self.multiworld.itempool.append(item)

    
from .client import TWEWYClient