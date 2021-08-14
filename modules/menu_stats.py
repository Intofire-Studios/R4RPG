from extensions.cmdClear import consoleClear

def menu_stats(p):
    consoleClear()
    print("---")
    print("Player stats!")
    print("---")
    print("Name: {}".format(p.name))
    print("Level: {}".format(p.level))
    print("XP: {}/{}".format(p.xp, p.max_xp))
    print("HP: {}/{}".format(p.hp,p.max_hp))
    print("Healing {}".format(p.heal_hp))
    print("Power {}".format(p.pw))
    input("Enter to continue.")