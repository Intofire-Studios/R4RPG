from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcshopupdate
from extensions.fileAssociation import saves, lastsavepath

def menu_resources_buy(p):
    saveProcess(p, saves, lastsavepath)
    rpcshopupdate(p)
    consoleClear()
    while p.money > 0:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(f"Choose resources! Money: {p.money}")
        print("---")
        print("1. Buy stone            [COST: 4]")
        print("2. Buy copper           [COST: 4]")
        print("3. Buy tin              [COST: 4]")
        print("4. Buy iron             [COST: 4]")
        print("5. Buy aluminum         [COST: 4]")
        print("6. Buy silver           [COST: 4]")
        print("7. Buy topaz            [COST: 4]")
        print("8. Buy gold             [COST: 4]")
        print("9. Buy crystal          [COST: 4]")
        print("10. Buy diamond         [COST: 4]")
        print("11. Buy ruby            [COST: 4]")
        print("12. Buy emerald         [COST: 4]")
        print("13. Exit to shop menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.money >= 4:
                p.money -= 4
                p.stone += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "2":
            if p.money >= 4:
                p.money -= 4
                p.copper += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "3":
            if p.money >= 4:
                p.money -= 4
                p.tin += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "4":
            if p.money >= 4:
                p.money -= 4
                p.iron += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "5":
            if p.money >= 4:
                p.money -= 4
                p.aluminum += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "6":
            if p.money >= 4:
                p.money -= 4
                p.silver += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "7":
            if p.money >= 4:
                p.money -= 4
                p.topaz += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "8":
            if p.money >= 4:
                p.money -= 4
                p.gold += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "9":
            if p.money >= 4:
                p.money -= 4
                p.crystal += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "10":
            if p.money >= 4:
                p.money -= 4
                p.diamond += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "11":
            if p.money >= 4:
                p.money -= 4
                p.ruby += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "12":
            if p.money >= 4:
                p.money -= 4
                p.emerald += 1
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "13":
            rpcshopupdate(p)
            break
        rpcshopupdate(p)
    consoleClear()
    saveProcess(p, saves, lastsavepath)