# Location name to Archipelago location ID mapping
location_name_to_id = {
    # Unique story beat locations
    "(S) Dash": 0xC0DE0000,
    "(B) Escaping from Battle": 0xC0DE0001,
    "(B) Bottom-screen Combat": 0xC0DE0002,
    "(B) Boot/Reboot": 0xC0DE0003,
    "(B) CONTROLS / Drag": 0xC0DE0004,
    "(B) Top-screen Combat": 0xC0DE0005,
    "(B) Dual-screen Combat": 0xC0DE0006,
    "(B) So I Beat the Enemy...": 0xC0DE0007,
    "(B) Follow That Puck!": 0xC0DE0008,
    "(B) Scanning": 0xC0DE0009,
    "(B) Enemy Encounters": 0xC0DE000A,
    "(B) CONTROLS / Touch": 0xC0DE000B,
    "(B) Use Obstacles": 0xC0DE000C,
    "(B) CONTROLS / Slash": 0xC0DE000D,
    "(B) Mail Icon": 0xC0DE000E,
    "(S) Phone Menu": 0xC0DE000F,
    "(B) Wearing Pins": 0xC0DE0010,
    "(S) Shutdown": 0xC0DE0011,
    "(B) Shutdown": 0xC0DE0012,
    "(S) Easy": 0xC0DE0013,
    "(B) Talk to Your Partner": 0xC0DE0014,
    "(B) Shop Clerks": 0xC0DE0015,
    "(B) Item Abilities": 0xC0DE0016,
    "(S) ESP Cards": 0xC0DE0017,
    "(S) Fusion Boost (Shiki)": 0xC0DE0018,
    "(B) Red Noise Symbols": 0xC0DE0019,
    "(B) Yellow Noise Symbols": 0xC0DE001A,
    "(S) Jump": 0xC0DE001B,
    "(B) Memes": 0xC0DE001C,
    "(S) Noise Report": 0xC0DE001D,
    "(S) Brand Awareness": 0xC0DE001E,
    "(B) Shop Quests": 0xC0DE001F,
    "(B) Green Noise Symbols": 0xC0DE0020,
    "(B) Pin Growth/Evolution": 0xC0DE0021,
    "(S) Chain 4": 0xC0DE0022,
    "(S) Backlash": 0xC0DE0023,
    "(B) Chained Battles": 0xC0DE0024,
    "(S) Mingle Mode": 0xC0DE0025,
    "(S) Block": 0xC0DE0026,
    "(S) Retry Battles": 0xC0DE0027,
    "(S) Safe Landing (Shiki)": 0xC0DE0028,
    "(B) Be a Trendsetter": 0xC0DE0029,
    # Stackable item locations
    "(S) Extra Slot 1": 0xC0DE002A,
    "(S) Extra Slot 2": 0xC0DE002B,
    "(S) DEF Boost (Shiki) 1": 0xC0DE002C,
    "(S) DEF Boost (Shiki) 2": 0xC0DE002D,
    "(S) DEF Boost (Shiki) 3": 0xC0DE002E,
    "(S) DEF Boost (Shiki) 4": 0xC0DE002F,
    "(S) DEF Boost (Shiki) 5": 0xC0DE0030,
    "(S) DEF Boost (Shiki) 6": 0xC0DE0031,
    "(S) DEF Boost (Shiki) 7": 0xC0DE0032,
    "(S) ATK Boost (Shiki) 1": 0xC0DE0033,
    "(S) ATK Boost (Shiki) 2": 0xC0DE0034,
    "(S) ATK Boost (Shiki) 3": 0xC0DE0035,
    "(S) ATK Boost (Shiki) 4": 0xC0DE0036,
    "(S) ATK Boost (Shiki) 5": 0xC0DE0037,
    "(S) ATK Boost (Shiki) 6": 0xC0DE0038,
}
 
# Location ID to combined index mapping for injection
# Stackable items use (combined_index, grant_number) tuples handled separately
LOCATION_TO_ITEM = {
    # Unique items
    0xC0DE0000: 0x2AD,  # (S) Dash
    0xC0DE0001: 0x2E1,  # (B) Escaping from Battle
    0xC0DE0002: 0x2D3,  # (B) Bottom-screen Combat
    0xC0DE0003: 0x2DD,  # (B) Boot/Reboot
    0xC0DE0004: 0x2D6,  # (B) CONTROLS / Drag
    0xC0DE0005: 0x2D2,  # (B) Top-screen Combat
    0xC0DE0006: 0x2D1,  # (B) Dual-screen Combat
    0xC0DE0007: 0x2D5,  # (B) So I Beat the Enemy...
    0xC0DE0008: 0x2D4,  # (B) Follow That Puck!
    0xC0DE0009: 0x2E2,  # (B) Scanning
    0xC0DE000A: 0x2E3,  # (B) Enemy Encounters
    0xC0DE000B: 0x2D7,  # (B) CONTROLS / Touch
    0xC0DE000C: 0x2DA,  # (B) Use Obstacles
    0xC0DE000D: 0x2D8,  # (B) CONTROLS / Slash
    0xC0DE000E: 0x2EC,  # (B) Mail Icon
    0xC0DE000F: 0x2A7,  # (S) Phone Menu
    0xC0DE0010: 0x2DB,  # (B) Wearing Pins
    0xC0DE0011: 0x2AB,  # (S) Shutdown
    0xC0DE0012: 0x2EE,  # (B) Shutdown
    0xC0DE0013: 0x2CD,  # (S) Easy
    0xC0DE0014: 0x2EB,  # (B) Talk to Your Partner
    0xC0DE0015: 0x2EF,  # (B) Shop Clerks
    0xC0DE0016: 0x2F0,  # (B) Item Abilities
    0xC0DE0017: 0x2AF,  # (S) ESP Cards
    0xC0DE0018: 0x2B0,  # (S) Fusion Boost (Shiki)
    0xC0DE0019: 0x2E5,  # (B) Red Noise Symbols
    0xC0DE001A: 0x2E8,  # (B) Yellow Noise Symbols
    0xC0DE001B: 0x2B6,  # (S) Jump
    0xC0DE001C: 0x2EA,  # (B) Memes
    0xC0DE001D: 0x2CE,  # (S) Noise Report
    0xC0DE001E: 0x2AC,  # (S) Brand Awareness
    0xC0DE001F: 0x2F1,  # (B) Shop Quests
    0xC0DE0020: 0x2E7,  # (B) Green Noise Symbols
    0xC0DE0021: 0x2DF,  # (B) Pin Growth/Evolution
    0xC0DE0022: 0x2C7,  # (S) Chain 4
    0xC0DE0023: 0x2B4,  # (S) Backlash
    0xC0DE0024: 0x2E4,  # (B) Chained Battles
    0xC0DE0025: 0x2D0,  # (S) Mingle Mode
    0xC0DE0026: 0x2B5,  # (S) Block
    0xC0DE0027: 0x2C9,  # (S) Retry Battles
    0xC0DE0028: 0x2B1,  # (S) Safe Landing (Shiki)
    0xC0DE0029: 0x2ED,  # (B) Be a Trendsetter
    # Stackable items - all map to same combined index
    0xC0DE002A: 0x2A8,  # (S) Extra Slot 1
    0xC0DE002B: 0x2A8,  # (S) Extra Slot 2
    0xC0DE002C: 0x2B3,  # (S) DEF Boost (Shiki) 1
    0xC0DE002D: 0x2B3,  # (S) DEF Boost (Shiki) 2
    0xC0DE002E: 0x2B3,  # (S) DEF Boost (Shiki) 3
    0xC0DE002F: 0x2B3,  # (S) DEF Boost (Shiki) 4
    0xC0DE0030: 0x2B3,  # (S) DEF Boost (Shiki) 5
    0xC0DE0031: 0x2B3,  # (S) DEF Boost (Shiki) 6
    0xC0DE0032: 0x2B3,  # (S) DEF Boost (Shiki) 7
    0xC0DE0033: 0x2B2,  # (S) ATK Boost (Shiki) 1
    0xC0DE0034: 0x2B2,  # (S) ATK Boost (Shiki) 2
    0xC0DE0035: 0x2B2,  # (S) ATK Boost (Shiki) 3
    0xC0DE0036: 0x2B2,  # (S) ATK Boost (Shiki) 4
    0xC0DE0037: 0x2B2,  # (S) ATK Boost (Shiki) 5
    0xC0DE0038: 0x2B2,  # (S) ATK Boost (Shiki) 6
}