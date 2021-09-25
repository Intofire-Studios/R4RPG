from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcshopupdate
from extensions.fileAssociation import saves

def menu_pickaxes(p):
    cfgsave(p, saves)
    rpcshopupdate(p)
    consoleClear()
    while p.money > 0:
        cfgsave(p, saves)
        print("---")
        print("Choose your next pickaxe! Money: {}".format(p.money))
        print("---")
        print("1. Wooden pickaxe    (Toughness: 10)       [COST: 2]")
        print("2. Stone pickaxe     (Toughness: 25)       [COST: 4]")
        print("3. Iron pickaxe      (Toughness: 50)       [COST: 7]")
        print("4. Golden pickaxe    (Toughness: 65)       [COST: 9]")
        print("5. Emerald pickaxe   (Toughness: 80)       [COST: 12]")
        print("6. Diamond pickaxe   (Toughness: 100)      [COST: 17]")
        print("7. Obsidian pickaxe  (Toughness: 200)      [COST: 30]")
        print("8. Exit to shop menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.money >= 2:
                p.money -= 2
                p.pickaxe, p.max_pickaxe = 10, 10
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "2":
            if p.money >= 4:
                p.money -= 4
                p.pickaxe, p.max_pickaxe = 25, 25
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "3":
            if p.money >= 7:
                p.money -= 7
                p.pickaxe, p.max_pickaxe = 50, 50
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "4":
            if p.money >= 9:
                p.money -= 9
                p.pickaxe, p.max_pickaxe = 65, 65
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "5":
            if p.money >= 12:
                p.money -= 12
                p.pickaxe, p.max_pickaxe = 80, 80
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "6":
            if p.money >= 17:
                p.money -= 17
                p.pickaxe, p.max_pickaxe = 100, 100
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "7":
            if p.money >= 30:
                p.money -= 30
                p.pickaxe, p.max_pickaxe = 200, 200
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "8":
            rpcshopupdate(p)
            break
        rpcshopupdate(p)
    consoleClear()
    cfgsave(p, saves)