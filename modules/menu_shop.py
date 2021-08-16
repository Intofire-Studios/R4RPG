from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcupdate

def menu_shop(p):
    consoleClear()
    while p.money > 0:
        print("---")
        print("Choose items! Money: {}".format(p.money))
        print("---")
        print("[COST: 5] 1. Power potion (+5 to power for one fight) — {} in the inventory".format(p.pwpotion))
        print("[COST: 1] 2. 5 heal potions (+{} to HP) — {} in the inventory".format(p.heal_hp, p.hppotion))
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.money >= 5:
                p.money -= 5
                p.pwpotion += 1
                rpcupdate(p)
            else:
                print("---")
                print("Not enough money.")
                rpcupdate(p)
        if n == "2":
            p.hppotion += 5
            p.money -= 1
            rpcupdate(p)
    consoleClear()