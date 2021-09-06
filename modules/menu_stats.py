from extensions.richPresence import rpcstatsupdate
from extensions.cmdClear import consoleClear

def menu_stats(p):
    rpcstatsupdate(p)
    consoleClear()
    print("---")
    print("Player stats!")
    print("---")
    print("Name: {}".format(p.name))
    print("Class: {}".format(p.cls))
    print("Level: {}".format(p.level))
    print("XP: {}/{}".format(p.xp, p.max_xp))
    print("HP: {}/{}".format(p.hp,p.max_hp))
    print("Power: {}".format(p.pw))
    print("Healing: {}".format(p.heal_hp))
    print("Power boost: {}".format(p.plus_pw))
    print("---")
    print("Power potions: {}".format(p.pwpotion))
    print("Heal potions: {}".format(p.hppotion))
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