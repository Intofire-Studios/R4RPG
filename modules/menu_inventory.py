from extensions.richPresence import rpcinventoryupdate
from extensions.cmdClear import consoleClear

def menu_inventory(p):
    rpcinventoryupdate(p)
    consoleClear()
    print("---")
    print("{}'s inventory!".format(p.name))
    print("---")
    print("Pickaxe: {}/{}".format(p.pickaxe, p.max_pickaxe))
    print("---")
    if p.stone != 0:
        print("Stone: {}".format(p.stone))
    if p.copper != 0:
        print("Сopper: {}".format(p.copper))
    if p.tin != 0:
        print("Tin: {}".format(p.tin))
    if p.iron != 0:
        print("Iron: {}".format(p.iron))
    if p.aluminum != 0:
        print("Aluminum: {}".format(p.aluminum))
    if p.silver != 0:
        print("Silver: {}".format(p.silver))
    if p.topaz != 0:
        print("Topaz: {}".format(p.topaz))
    if p.gold != 0:
        print("Gold: {}".format(p.gold))
    if p.crystal != 0:
        print("Crystal: {}".format(p.crystal))
    if p.diamond != 0:
        print("Diamond: {}".format(p.diamond))
    if p.ruby != 0:
        print("Ruby: {}".format(p.ruby))
    if p.emerald != 0:
        print("Emerald: {}".format(p.emerald))
    print("---")
    input("Enter to continue.")
    consoleClear()