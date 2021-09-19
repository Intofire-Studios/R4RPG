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
    print("Stone: {}".format(p.stone))
    print("---")
    input("Enter to continue.")
    consoleClear()