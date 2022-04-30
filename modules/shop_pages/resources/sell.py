from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath

def menu_resources_sell(p):
    saveProcess(p, saves, lastsavepath)
    consoleClear()
    while p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver > 0:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(f"Choose what you want to sell! Money: {p.money}")
        print("---")
        print("1. Sell stone            [COST: 2]")
        print("2. Sell copper           [COST: 2]")
        print("3. Sell tin              [COST: 2]")
        print("4. Sell iron             [COST: 2]")
        print("5. Sell aluminum         [COST: 2]")
        print("6. Sell silver           [COST: 2]")
        print("7. Sell topaz            [COST: 2]")
        print("8. Sell gold             [COST: 2]")
        print("9. Sell crystal          [COST: 2]")
        print("10. Sell diamond         [COST: 2]")
        print("11. Sell ruby            [COST: 2]")
        print("12. Sell emerald         [COST: 2]")
        print("13. Exit to shop menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.stone > 0:
                p.stone -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough stone.")
        if n == "2":
            if p.copper > 0:
                p.money += 2
                p.copper -= 1
            else:
                print("---")
                print("Not enough copper.")
        if n == "3":
            if p.tin > 0:
                p.tin -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough tin.")
        if n == "4":
            if p.iron > 0:
                p.iron -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough iron.")
        if n == "5":
            if p.aluminum > 0:
                p.aluminum -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough aluminum.")
        if n == "6":
            if p.silver > 0:
                p.silver -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough silver.")
        if n == "7":
            if p.topaz > 0:
                p.topaz -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough topaz.")
        if n == "8":
            if p.gold > 0:
                p.gold -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough gold.")
        if n == "9":
            if p.crystal > 0:
                p.crystal -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough crystal.")
        if n == "10":
            if p.diamond > 0:
                p.diamond -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough diamond.")
        if n == "11":
            if p.ruby > 0:
                p.ruby -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough ruby.")
        if n == "12":
            if p.emerald > 0:
                p.emerald -= 1
                p.money += 2
            else:
                print("---")
                print("Not enough emerald.")
        if n == "13":
            rpcshopupdate(p)
            break
    consoleClear()
    saveProcess(p, saves, lastsavepath)