# Item <-> location mappings
ITEM_TO_LOCATION = {
    0x2E1: 0xC0DE0000,  # (B) Escaping from Battle
    0x2AD: 0xC0DE0001,  # (S) Dash
    0x2A3: 0xC0DE0002,  # (CD) Track 31
    0x282: 0xC0DE0003,  # My First Wallet
    0x2D3: 0xC0DE0004,  # (B) Bottom-screen Combat
    0x2DD: 0xC0DE0005,  # (B) Boot/Reboot
    0x2D6: 0xC0DE0006,  # (B) CONTROLS / Drag
    0x2D2: 0xC0DE0007,  # (B) Top-screen Combat
    0x2D1: 0xC0DE0008,  # (B) Dual-screen Combat
    0x2D4: 0xC0DE0009,  # (B) Follow That Puck!
    0x2D5: 0xC0DE000A,  # (B) So I Beat the Enemy...
    0x2E2: 0xC0DE000B,  # (B) Scanning
    0x2E3: 0xC0DE000C,  # (B) Enemy Encounters
    0x2D7: 0xC0DE000D,  # (B) CONTROLS / Touch
    0x2DA: 0xC0DE000E,  # (B) Use Obstacles
    0x2D8: 0xC0DE000F,  # (B) CONTROLS / Slash
    0x2EC: 0xC0DE0010,  # (B) Mail Icon
    0x2A7: 0xC0DE0011,  # (S) Phone Menu
    0x2DB: 0xC0DE0012,  # (B) Wearing Pins
    0x2A8: 0xC0DE0013,  # (S) Extra Slot
    0x2B3: 0xC0DE0014,  # (S) DEF Boost (Shiki)
    0x2B2: 0xC0DE0015,  # (S) ATK Boost (Shiki)
    0x2AB: 0xC0DE0016,  # (S) Shutdown
    0x2EE: 0xC0DE0017,  # (B) Shutdown
    0x2CD: 0xC0DE0018,  # (S) Easy
    0x2EB: 0xC0DE0019,  # (B) Talk to Your Partner
    0x2F0: 0xC0DE001A,  # (B) Item Abilities
    0x2EF: 0xC0DE001B,  # (B) Shop Clerks
    0x2B0: 0xC0DE001C,  # (S) Fusion Boost (Shiki)
    0x2AF: 0xC0DE001D,  # (S) ESP Cards
    0x2E8: 0xC0DE001E,  # (B) Yellow Noise Symbols
    0x2E5: 0xC0DE001F,  # (B) Red Noise Symbols
    0x2B6: 0xC0DE0020,  # (S) Jump
    0x2EA: 0xC0DE0021,  # (B) Memes
    0x2CE: 0xC0DE0022,  # (S) Noise Report
    0x2AC: 0xC0DE0023,  # (S) Brand Awareness
    0x2F1: 0xC0DE0024,  # (B) Shop Quests
    0x2E7: 0xC0DE0025,  # (B) Green Noise Symbols
    0x2DF: 0xC0DE0026,  # (B) Pin Growth/Evolution
    0x2C7: 0xC0DE0027,  # (S) Chain 4
    0x2B4: 0xC0DE0028,  # (S) Backlash
    0x2E4: 0xC0DE0029,  # (B) Chained Battles
    0x2D0: 0xC0DE002A,  # (S) Mingle Mode
    0x278: 0xC0DE002B,  # Durable Leather
    0x2B5: 0xC0DE002C,  # (S) Block
    0x2C9: 0xC0DE002D,  # (S) Retry Battles
    0x2B1: 0xC0DE002E,  # (S) Safe Landing (Shiki)
    0x2A9: 0xC0DE002F,  # (S) Safe Landing (Neku)
    0x273: 0xC0DE0030,  # Sleek Silk
    0x285: 0xC0DE0031,  # (CD) Track 1
    0x29A: 0xC0DE0032,  # (CD) Track 22
    0x2ED: 0xC0DE0033,  # (B) Be a Trendsetter
}

item_name_to_id = {
    "(B) Escaping from Battle": 0xC0DE0000,
    "(S) Dash": 0xC0DE0001,
    "(CD) Track 31": 0xC0DE0002,
    "My First Wallet": 0xC0DE0003,
    "(B) Bottom-screen Combat": 0xC0DE0004,
    "(B) Boot/Reboot": 0xC0DE0005,
    "(B) CONTROLS / Drag": 0xC0DE0006,
    "(B) Top-screen Combat": 0xC0DE0007,
    "(B) Dual-screen Combat": 0xC0DE0008,
    "(B) Follow That Puck!": 0xC0DE0009,
    "(B) So I Beat the Enemy...": 0xC0DE000A,
    "(B) Scanning": 0xC0DE000B,
    "(B) Enemy Encounters": 0xC0DE000C,
    "(B) CONTROLS / Touch": 0xC0DE000D,
    "(B) Use Obstacles": 0xC0DE000E,
    "(B) CONTROLS / Slash": 0xC0DE000F,
    "(B) Mail Icon": 0xC0DE0010,
    "(S) Phone Menu": 0xC0DE0011,
    "(B) Wearing Pins": 0xC0DE0012,
    "(S) Extra Slot": 0xC0DE0013,
    "(S) DEF Boost (Shiki)": 0xC0DE0014,
    "(S) ATK Boost (Shiki)": 0xC0DE0015,
    "(S) Shutdown": 0xC0DE0016,
    "(B) Shutdown": 0xC0DE0017,
    "(S) Easy": 0xC0DE0018,
    "(B) Talk to Your Partner": 0xC0DE0019,
    "(B) Item Abilities": 0xC0DE001A,
    "(B) Shop Clerks": 0xC0DE001B,
    "(S) Fusion Boost (Shiki)": 0xC0DE001C,
    "(S) ESP Cards": 0xC0DE001D,
    "(B) Yellow Noise Symbols": 0xC0DE001E,
    "(B) Red Noise Symbols": 0xC0DE001F,
    "(S) Jump": 0xC0DE0020,
    "(B) Memes": 0xC0DE0021,
    "(S) Noise Report": 0xC0DE0022,
    "(S) Brand Awareness": 0xC0DE0023,
    "(B) Shop Quests": 0xC0DE0024,
    "(B) Green Noise Symbols": 0xC0DE0025,
    "(B) Pin Growth/Evolution": 0xC0DE0026,
    "(S) Chain 4": 0xC0DE0027,
    "(S) Backlash": 0xC0DE0028,
    "(B) Chained Battles": 0xC0DE0029,
    "(S) Mingle Mode": 0xC0DE002A,
    "Durable Leather": 0xC0DE002B,
    "(S) Block": 0xC0DE002C,
    "(S) Retry Battles": 0xC0DE002D,
    "(S) Safe Landing (Shiki)": 0xC0DE002E,
    "(S) Safe Landing (Neku)": 0xC0DE002F,
    "Sleek Silk": 0xC0DE0030,
    "(CD) Track 1": 0xC0DE0031,
    "(CD) Track 22": 0xC0DE0032,
    "(B) Be a Trendsetter": 0xC0DE0033,
    }