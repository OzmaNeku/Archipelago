from BaseClasses import ItemClassification

location_name_to_id = {
    # Week 1 Day 1
    "W1D1: Dash":                   0xC0DE0000,
    "W1D1: Escaping from Battle":   0xC0DE0001,
    "W1D1: My First Wallet":        0xC0DE0002,
    "W1D1: CD Track 31":            0xC0DE0003,
    "W1D1: Bottom-screen Combat":   0xC0DE0004,
    "W1D1: Boot/Reboot":            0xC0DE0005,
    "W1D1: CONTROLS / Drag":        0xC0DE0006,
    "W1D1: Top-screen Combat":      0xC0DE0007,
    "W1D1: Dual-screen Combat":     0xC0DE0008,
    "W1D1: So I Beat the Enemy...": 0xC0DE0009,
    "W1D1: Follow That Puck!":      0xC0DE000A,
    # Week 1 Day 2
    "W1D2: Scanning":               0xC0DE000B,
    "W1D2: Enemy Encounters":       0xC0DE000C,
    "W1D2: CONTROLS / Touch":       0xC0DE000D,
    "W1D2: Use Obstacles":          0xC0DE000E,
    "W1D2: CONTROLS / Slash":       0xC0DE000F,
    "W1D2: Mail Icon":              0xC0DE0010,
    "W1D2: Phone Menu":             0xC0DE0011,
    "W1D2: Wearing Pins":           0xC0DE0012,
    "W1D2: Extra Slot 1":           0xC0DE0013,
    "W1D2: DEF Boost (Shiki) 1":    0xC0DE0014,
    "W1D2: ATK Boost (Shiki) 1":    0xC0DE0015,
    # Week 1 Day 3
    "W1D3: Shutdown (S)":           0xC0DE0016,
    "W1D3: Shutdown (B)":           0xC0DE0017,
    "W1D3: Easy":                   0xC0DE0018,
    "W1D3: Talk to Your Partner":   0xC0DE0019,
    "W1D3: Shop Clerks":            0xC0DE001A,
    "W1D3: Item Abilities":         0xC0DE001B,
    "W1D3: ESP Cards":              0xC0DE001C,
    "W1D3: Fusion Boost (Shiki)":   0xC0DE001D,
    "W1D3: DEF Boost (Shiki) 2":    0xC0DE001E,
    "W1D3: Red Noise Symbols":      0xC0DE001F,
    "W1D3: Yellow Noise Symbols":   0xC0DE0020,
    "W1D3: Jump":                   0xC0DE0021,
    "W1D3: Memes":                  0xC0DE0022,
    "W1D3: ATK Boost (Shiki) 2":    0xC0DE0023,
    # Week 1 Day 4
    "W1D4: Noise Report":           0xC0DE0024,
    "W1D4: Brand Awareness":        0xC0DE0025,
    "W1D4: Shop Quests":            0xC0DE0026,
    "W1D4: Green Noise Symbols":    0xC0DE0027,
    "W1D4: Pin Growth/Evolution":   0xC0DE0028,
    "W1D4: Extra Slot 2":           0xC0DE0029,
    "W1D4: Chain 4":                0xC0DE002A,
    "W1D4: Backlash":               0xC0DE002B,
    "W1D4: DEF Boost (Shiki) 3":    0xC0DE002C,
    "W1D4: Chained Battles":        0xC0DE002D,
    "W1D4: Mingle Mode":            0xC0DE002E,
    "W1D4: ATK Boost (Shiki) 3":    0xC0DE002F,
    # Week 1 Day 5
    "W1D5: Block":                  0xC0DE0030,
    "W1D5: DEF Boost (Shiki) 4":    0xC0DE0031,
    "W1D5: ATK Boost (Shiki) 4":    0xC0DE0032,
    "W1D5: Retry Battles":          0xC0DE0033,
    # Week 1 Day 6
    "W1D6: Safe Landing (Shiki)":   0xC0DE0034,
    "W1D6: DEF Boost (Shiki) 5":    0xC0DE0035,
    "W1D6: ATK Boost (Shiki) 5":    0xC0DE0036,
    "W1D6: Be a Trendsetter":       0xC0DE0037,
    # Week 1 Day 7
    "W1D7: ATK Boost (Shiki) 6":    0xC0DE0038,
    "W1D7: DEF Boost (Shiki) 6":    0xC0DE0039,
}

# Location ID to combined index mapping for item injection
LOCATION_TO_ITEM = {
    0xC0DE0000: 0x2AD,  # (S) Dash
    0xC0DE0001: 0x2E1,  # (B) Escaping from Battle
    0xC0DE0002: 0x282,  # My First Wallet
    0xC0DE0003: 0x2A3,  # (CD) Track 31
    0xC0DE0004: 0x2D3,  # (B) Bottom-screen Combat
    0xC0DE0005: 0x2DD,  # (B) Boot/Reboot
    0xC0DE0006: 0x2D6,  # (B) CONTROLS / Drag
    0xC0DE0007: 0x2D2,  # (B) Top-screen Combat
    0xC0DE0008: 0x2D1,  # (B) Dual-screen Combat
    0xC0DE0009: 0x2D5,  # (B) So I Beat the Enemy...
    0xC0DE000A: 0x2D4,  # (B) Follow That Puck!
    0xC0DE000B: 0x2E2,  # (B) Scanning
    0xC0DE000C: 0x2E3,  # (B) Enemy Encounters
    0xC0DE000D: 0x2D7,  # (B) CONTROLS / Touch
    0xC0DE000E: 0x2DA,  # (B) Use Obstacles
    0xC0DE000F: 0x2D8,  # (B) CONTROLS / Slash
    0xC0DE0010: 0x2EC,  # (B) Mail Icon
    0xC0DE0011: 0x2A7,  # (S) Phone Menu
    0xC0DE0012: 0x2DB,  # (B) Wearing Pins
    0xC0DE0013: 0x2A8,  # (S) Extra Slot
    0xC0DE0014: 0x2B3,  # (S) DEF Boost (Shiki)
    0xC0DE0015: 0x2B2,  # (S) ATK Boost (Shiki)
    0xC0DE0016: 0x2AB,  # (S) Shutdown
    0xC0DE0017: 0x2EE,  # (B) Shutdown
    0xC0DE0018: 0x2CD,  # (S) Easy
    0xC0DE0019: 0x2EB,  # (B) Talk to Your Partner
    0xC0DE001A: 0x2EF,  # (B) Shop Clerks
    0xC0DE001B: 0x2F0,  # (B) Item Abilities
    0xC0DE001C: 0x2AF,  # (S) ESP Cards
    0xC0DE001D: 0x2B0,  # (S) Fusion Boost (Shiki)
    0xC0DE001E: 0x2B3,  # (S) DEF Boost (Shiki)
    0xC0DE001F: 0x2E5,  # (B) Red Noise Symbols
    0xC0DE0020: 0x2E8,  # (B) Yellow Noise Symbols
    0xC0DE0021: 0x2B6,  # (S) Jump
    0xC0DE0022: 0x2EA,  # (B) Memes
    0xC0DE0023: 0x2B2,  # (S) ATK Boost (Shiki)
    0xC0DE0024: 0x2CE,  # (S) Noise Report
    0xC0DE0025: 0x2AC,  # (S) Brand Awareness
    0xC0DE0026: 0x2F1,  # (B) Shop Quests
    0xC0DE0027: 0x2E7,  # (B) Green Noise Symbols
    0xC0DE0028: 0x2DF,  # (B) Pin Growth/Evolution
    0xC0DE0029: 0x2A8,  # (S) Extra Slot
    0xC0DE002A: 0x2C7,  # (S) Chain 4
    0xC0DE002B: 0x2B4,  # (S) Backlash
    0xC0DE002C: 0x2B3,  # (S) DEF Boost (Shiki)
    0xC0DE002D: 0x2E4,  # (B) Chained Battles
    0xC0DE002E: 0x2D0,  # (S) Mingle Mode
    0xC0DE002F: 0x2B2,  # (S) ATK Boost (Shiki)
    0xC0DE0030: 0x2B5,  # (S) Block
    0xC0DE0031: 0x2B3,  # (S) DEF Boost (Shiki)
    0xC0DE0032: 0x2B2,  # (S) ATK Boost (Shiki)
    0xC0DE0033: 0x2C9,  # (S) Retry Battles
    0xC0DE0034: 0x2B1,  # (S) Safe Landing (Shiki)
    0xC0DE0035: 0x2B3,  # (S) DEF Boost (Shiki)
    0xC0DE0036: 0x2B2,  # (S) ATK Boost (Shiki)
    0xC0DE0037: 0x2ED,  # (B) Be a Trendsetter
    0xC0DE0038: 0x2B2,  # (S) ATK Boost (Shiki)
    0xC0DE0039: 0x2B3,  # (S) DEF Boost (Shiki)
}