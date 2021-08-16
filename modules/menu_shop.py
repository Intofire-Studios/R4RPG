from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcshopupdate, rpcupdate

def menu_shop(p):
    rpcshopupdate(p)
    consoleClear()
    while p.money > 0:
        print("---")
        print("Choose items! Money: {}".format(p.money))
        print("---")
        print("[COST: 5] 1. Power potion (+{} to Power for one fight) — {} in the inventory".format(p.plus_pw, p.pwpotion))
        print("[COST: 1] 2. 5 heal potions (+{} to HP) — {} in the inventory".format(p.heal_hp, p.hppotion))
        print("3. Exit to main menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.money >= 5:
                p.money -= 5
                p.pwpotion += 1
                rpcshopupdate(p)
            else:
                print("---")
                print("Not enough money.")
                rpcshopupdate(p)
        if n == "2":
            p.hppotion += 5
            p.money -= 1
            rpcshopupdate(p)
        if n == "3":
            break
    consoleClear()