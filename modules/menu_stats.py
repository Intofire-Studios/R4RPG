from extensions.richPresence import rpcstatsupdate
from extensions.cmdClear import consoleClear

def menu_stats(p):
    rpcstatsupdate(p)
    consoleClear()
    print("---")
    print("Player stats!")
    print("---")
    print(f"Name: {p.name}")
    print(f"Class: {p.cls}")
    print(f"Level: {p.level}")
    print(f"XP: {p.xp}/{p.max_xp}")
    print(f"HP: {p.hp}/{p.max_hp}")
    print(f"Power: {p.pw}")
    print(f"Healing: {p.heal_hp}")
    print(f"Power boost: {p.plus_pw}")
    print("---")
    print(f"Power potions: {p.pwpotion}")
    print(f"Heal potions: {p.hppotion}")
    print("---")
    print("Travel passes:")
    print("- Spawn Pass")
    if p.sandspass == 1:
        print("- Sands Pass")
    if p.snowkingdompass == 1:
        print("- Snow Kingdom Pass")
    print("---")
    input("Enter to continue.")
    consoleClear()