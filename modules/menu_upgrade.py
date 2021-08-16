from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcupdate

def menu_upgrade(p):
    while p.sp > 0:
        consoleClear()
        print("---")
        print("Choose your upgrades! Skill points: {}".format(p.sp))
        print("---")
        print("1. HP {}/{}".format(p.hp, p.max_hp))
        print("2. Power {}".format(p.pw))
        print("3. Heal points {}".format(p.heal_hp))
        n = input("Number: ")
        if n == "1":
            p.hp += 5
            p.sp -= 1
            p.max_hp += 5
            rpcupdate(p)
        if n == "2":
            p.pw += 1
            p.sp -= 1
            rpcupdate(p)
        if n == "3":
            p.heal_hp += 1
            p.sp -= 1
        consoleClear()
    consoleClear()