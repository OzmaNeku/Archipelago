ITEM_TO_LOCATION = {
    # Week 1 story drops - unique items
    0x2AD: 0xC0DE0000,  # (S) Dash
    0x2E1: 0xC0DE0001,  # (B) Escaping from Battle
    0x2D3: 0xC0DE0002,  # (B) Bottom-screen Combat
    0x2DD: 0xC0DE0003,  # (B) Boot/Reboot
    0x2D6: 0xC0DE0004,  # (B) CONTROLS / Drag
    0x2D2: 0xC0DE0005,  # (B) Top-screen Combat
    0x2D1: 0xC0DE0006,  # (B) Dual-screen Combat
    0x2D5: 0xC0DE0007,  # (B) So I Beat the Enemy...
    0x2D4: 0xC0DE0008,  # (B) Follow That Puck!
    0x2E2: 0xC0DE0009,  # (B) Scanning
    0x2E3: 0xC0DE000A,  # (B) Enemy Encounters
    0x2D7: 0xC0DE000B,  # (B) CONTROLS / Touch
    0x2DA: 0xC0DE000C,  # (B) Use Obstacles
    0x2D8: 0xC0DE000D,  # (B) CONTROLS / Slash
    0x2EC: 0xC0DE000E,  # (B) Mail Icon
    0x2A7: 0xC0DE000F,  # (S) Phone Menu
    0x2DB: 0xC0DE0010,  # (B) Wearing Pins
    0x2AB: 0xC0DE0011,  # (S) Shutdown
    0x2EE: 0xC0DE0012,  # (B) Shutdown
    0x2CD: 0xC0DE0013,  # (S) Easy
    0x2EB: 0xC0DE0014,  # (B) Talk to Your Partner
    0x2EF: 0xC0DE0015,  # (B) Shop Clerks
    0x2F0: 0xC0DE0016,  # (B) Item Abilities
    0x2AF: 0xC0DE0017,  # (S) ESP Cards
    0x2B0: 0xC0DE0018,  # (S) Fusion Boost (Shiki)
    0x2E5: 0xC0DE0019,  # (B) Red Noise Symbols
    0x2E8: 0xC0DE001A,  # (B) Yellow Noise Symbols
    0x2B6: 0xC0DE001B,  # (S) Jump
    0x2EA: 0xC0DE001C,  # (B) Memes
    0x2CE: 0xC0DE001D,  # (S) Noise Report
    0x2AC: 0xC0DE001E,  # (S) Brand Awareness
    0x2F1: 0xC0DE001F,  # (B) Shop Quests
    0x2E7: 0xC0DE0020,  # (B) Green Noise Symbols
    0x2DF: 0xC0DE0021,  # (B) Pin Growth/Evolution
    0x2C7: 0xC0DE0022,  # (S) Chain 4
    0x2B4: 0xC0DE0023,  # (S) Backlash
    0x2E4: 0xC0DE0024,  # (B) Chained Battles
    0x2D0: 0xC0DE0025,  # (S) Mingle Mode
    0x2B5: 0xC0DE0026,  # (S) Block
    0x2C9: 0xC0DE0027,  # (S) Retry Battles
    0x2B1: 0xC0DE0028,  # (S) Safe Landing (Shiki)
    0x2ED: 0xC0DE0029,  # (B) Be a Trendsetter
}
 
# Stackable items - each grant is a separate location ID
# Format: (combined_index, grant_number): location_id
STACKABLE_ITEM_TO_LOCATION = {
    (0x2A8, 1): 0xC0DE002A,  # (S) Extra Slot 1
    (0x2A8, 2): 0xC0DE002B,  # (S) Extra Slot 2
    (0x2B3, 1): 0xC0DE002C,  # (S) DEF Boost (Shiki) 1
    (0x2B3, 2): 0xC0DE002D,  # (S) DEF Boost (Shiki) 2
    (0x2B3, 3): 0xC0DE002E,  # (S) DEF Boost (Shiki) 3
    (0x2B3, 4): 0xC0DE002F,  # (S) DEF Boost (Shiki) 4
    (0x2B3, 5): 0xC0DE0030,  # (S) DEF Boost (Shiki) 5
    (0x2B3, 6): 0xC0DE0031,  # (S) DEF Boost (Shiki) 6
    (0x2B3, 7): 0xC0DE0032,  # (S) DEF Boost (Shiki) 7
    (0x2B2, 1): 0xC0DE0033,  # (S) ATK Boost (Shiki) 1
    (0x2B2, 2): 0xC0DE0034,  # (S) ATK Boost (Shiki) 2
    (0x2B2, 3): 0xC0DE0035,  # (S) ATK Boost (Shiki) 3
    (0x2B2, 4): 0xC0DE0036,  # (S) ATK Boost (Shiki) 4
    (0x2B2, 5): 0xC0DE0037,  # (S) ATK Boost (Shiki) 5
    (0x2B2, 6): 0xC0DE0038,  # (S) ATK Boost (Shiki) 6
}
 
# Item names for Archipelago item pool
item_name_to_id = {
    # Unique items
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
    # Stackable items
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