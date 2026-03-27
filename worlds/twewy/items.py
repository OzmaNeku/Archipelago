from BaseClasses import ItemClassification

# Combined index to location ID — unique items only
# Stackable items (Extra Slot, DEF Boost, ATK Boost) handled by ITEM_GRANT_TO_LOCATION
ITEM_TO_LOCATION = {
    0x2AD: 0xC0DE0000,  # (S) Dash
    0x2E1: 0xC0DE0001,  # (B) Escaping from Battle
    0x282: 0xC0DE0002,  # My First Wallet
    0x2A3: 0xC0DE0003,  # (CD) Track 31
    0x2D3: 0xC0DE0004,  # (B) Bottom-screen Combat
    0x2DD: 0xC0DE0005,  # (B) Boot/Reboot
    0x2D6: 0xC0DE0006,  # (B) CONTROLS / Drag
    0x2D2: 0xC0DE0007,  # (B) Top-screen Combat
    0x2D1: 0xC0DE0008,  # (B) Dual-screen Combat
    0x2D5: 0xC0DE0009,  # (B) So I Beat the Enemy...
    0x2D4: 0xC0DE000A,  # (B) Follow That Puck!
    0x2E2: 0xC0DE000B,  # (B) Scanning
    0x2E3: 0xC0DE000C,  # (B) Enemy Encounters
    0x2D7: 0xC0DE000D,  # (B) CONTROLS / Touch
    0x2DA: 0xC0DE000E,  # (B) Use Obstacles
    0x2D8: 0xC0DE000F,  # (B) CONTROLS / Slash
    0x2EC: 0xC0DE0010,  # (B) Mail Icon
    0x2A7: 0xC0DE0011,  # (S) Phone Menu
    0x2DB: 0xC0DE0012,  # (B) Wearing Pins
    0x2AB: 0xC0DE0016,  # (S) Shutdown
    0x2EE: 0xC0DE0017,  # (B) Shutdown
    0x2CD: 0xC0DE0018,  # (S) Easy
    0x2EB: 0xC0DE0019,  # (B) Talk to Your Partner
    0x2EF: 0xC0DE001A,  # (B) Shop Clerks
    0x2F0: 0xC0DE001B,  # (B) Item Abilities
    0x2AF: 0xC0DE001C,  # (S) ESP Cards
    0x2B0: 0xC0DE001D,  # (S) Fusion Boost (Shiki)
    0x2E5: 0xC0DE001F,  # (B) Red Noise Symbols
    0x2E8: 0xC0DE0020,  # (B) Yellow Noise Symbols
    0x2B6: 0xC0DE0021,  # (S) Jump
    0x2EA: 0xC0DE0022,  # (B) Memes
    0x2CE: 0xC0DE0024,  # (S) Noise Report
    0x2AC: 0xC0DE0025,  # (S) Brand Awareness
    0x2F1: 0xC0DE0026,  # (B) Shop Quests
    0x2E7: 0xC0DE0027,  # (B) Green Noise Symbols
    0x2DF: 0xC0DE0028,  # (B) Pin Growth/Evolution
    0x2C7: 0xC0DE002A,  # (S) Chain 4
    0x2B4: 0xC0DE002B,  # (S) Backlash
    0x2E4: 0xC0DE002D,  # (B) Chained Battles
    0x2D0: 0xC0DE002E,  # (S) Mingle Mode
    0x2B5: 0xC0DE0030,  # (S) Block
    0x2C9: 0xC0DE0033,  # (S) Retry Battles
    0x2B1: 0xC0DE0034,  # (S) Safe Landing (Shiki)
    0x2ED: 0xC0DE0037,  # (B) Be a Trendsetter
}

# Stackable items — each grant maps to a unique location
# Format: (combined_index, grant_number): location_id
ITEM_GRANT_TO_LOCATION = {
    (0x2A8, 1): 0xC0DE0013,  # Extra Slot 1
    (0x2A8, 2): 0xC0DE0029,  # Extra Slot 2
    (0x2B3, 1): 0xC0DE0014,  # DEF Boost (Shiki) 1
    (0x2B3, 2): 0xC0DE001E,  # DEF Boost (Shiki) 2
    (0x2B3, 3): 0xC0DE002C,  # DEF Boost (Shiki) 3
    (0x2B3, 4): 0xC0DE0031,  # DEF Boost (Shiki) 4
    (0x2B3, 5): 0xC0DE0035,  # DEF Boost (Shiki) 5
    (0x2B3, 6): 0xC0DE0039,  # DEF Boost (Shiki) 6
    (0x2B2, 1): 0xC0DE0015,  # ATK Boost (Shiki) 1
    (0x2B2, 2): 0xC0DE0023,  # ATK Boost (Shiki) 2
    (0x2B2, 3): 0xC0DE002F,  # ATK Boost (Shiki) 3
    (0x2B2, 4): 0xC0DE0032,  # ATK Boost (Shiki) 4
    (0x2B2, 5): 0xC0DE0036,  # ATK Boost (Shiki) 5
    (0x2B2, 6): 0xC0DE0038,  # ATK Boost (Shiki) 6
}

# Item name to Archipelago item ID
item_name_to_id = {
    # Progression
    "(S) Dash":                 0xC0DE0000,
    "(S) Phone Menu":           0xC0DE0011,
    "(S) Shutdown":             0xC0DE0016,
    "(S) Easy":                 0xC0DE0018,
    "(S) ESP Cards":            0xC0DE001C,
    "(S) Noise Report":         0xC0DE0024,
    "(S) Mingle Mode":          0xC0DE002E,
    "(S) Extra Slot":           0xC0DE0013,
    # Useful
    "My First Wallet":          0xC0DE0002,
    "(S) Fusion Boost (Shiki)": 0xC0DE001D,
    "(S) Jump":                 0xC0DE0021,
    "(S) Brand Awareness":      0xC0DE0025,
    "(S) Chain 4":              0xC0DE002A,
    "(S) Backlash":             0xC0DE002B,
    "(S) Block":                0xC0DE0030,
    "(S) Retry Battles":        0xC0DE0033,
    "(S) Safe Landing (Shiki)": 0xC0DE0034,
    "(S) DEF Boost (Shiki)":    0xC0DE0014,
    "(S) ATK Boost (Shiki)":    0xC0DE0015,
    # Filler
    "(B) Escaping from Battle": 0xC0DE0001,
    "(CD) Track 31":            0xC0DE0003,
    "(B) Bottom-screen Combat": 0xC0DE0004,
    "(B) Boot/Reboot":          0xC0DE0005,
    "(B) CONTROLS / Drag":      0xC0DE0006,
    "(B) Top-screen Combat":    0xC0DE0007,
    "(B) Dual-screen Combat":   0xC0DE0008,
    "(B) So I Beat the Enemy...": 0xC0DE0009,
    "(B) Follow That Puck!":    0xC0DE000A,
    "(B) Scanning":             0xC0DE000B,
    "(B) Enemy Encounters":     0xC0DE000C,
    "(B) CONTROLS / Touch":     0xC0DE000D,
    "(B) Use Obstacles":        0xC0DE000E,
    "(B) CONTROLS / Slash":     0xC0DE000F,
    "(B) Mail Icon":            0xC0DE0010,
    "(B) Wearing Pins":         0xC0DE0012,
    "(B) Shutdown":             0xC0DE0017,
    "(B) Talk to Your Partner": 0xC0DE0019,
    "(B) Shop Clerks":          0xC0DE001A,
    "(B) Item Abilities":       0xC0DE001B,
    "(B) Red Noise Symbols":    0xC0DE001F,
    "(B) Yellow Noise Symbols": 0xC0DE0020,
    "(B) Memes":                0xC0DE0022,
    "(B) Shop Quests":          0xC0DE0026,
    "(B) Green Noise Symbols":  0xC0DE0027,
    "(B) Pin Growth/Evolution": 0xC0DE0028,
    "(B) Chained Battles":      0xC0DE002D,
    "(B) Be a Trendsetter":     0xC0DE0037,
}

# Item classifications
item_classifications = {
    # Progression
    "(S) Dash":                 ItemClassification.progression,
    "(S) Phone Menu":           ItemClassification.progression,
    "(S) Shutdown":             ItemClassification.progression,
    "(S) Easy":                 ItemClassification.progression,
    "(S) ESP Cards":            ItemClassification.progression,
    "(S) Noise Report":         ItemClassification.progression,
    "(S) Mingle Mode":          ItemClassification.progression,
    "(S) Extra Slot":           ItemClassification.progression,
    # Useful
    "My First Wallet":          ItemClassification.useful,
    "(S) Fusion Boost (Shiki)": ItemClassification.useful,
    "(S) Jump":                 ItemClassification.useful,
    "(S) Brand Awareness":      ItemClassification.useful,
    "(S) Chain 4":              ItemClassification.useful,
    "(S) Backlash":             ItemClassification.useful,
    "(S) Block":                ItemClassification.useful,
    "(S) Retry Battles":        ItemClassification.useful,
    "(S) Safe Landing (Shiki)": ItemClassification.useful,
    "(S) DEF Boost (Shiki)":    ItemClassification.useful,
    "(S) ATK Boost (Shiki)":    ItemClassification.useful,
}