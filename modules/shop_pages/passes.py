from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcshopupdate
from extensions.fileAssociation import saves, lastsavepath

def menu_passes(p):
    saveProcess(p, saves, lastsavepath)
    rpcshopupdate(p)
    consoleClear()
    while p.money > 0:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(f"Choose passes! Money: {p.money}")
        print("---")
        if p.sandspass != 1:
            print("1. Sands Pass          [COST: 100]")
        else:
            print("1. Sands Pass          [PURCHASED]")
        if p.snowkingdompass != 1:
            print("2. Snow Kingdom Pass   [COST: 250]")
        else:
            print("2. Snow Kingdom Pass   [PURCHASED]")
        print("3. Exit to shop menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.money >= 100 and p.sandspass != 1:
                p.money -= 100
                p.sandspass = 1
            elif p.sandspass == 1:
                print("---")
                print("This travel pass is already purchased.")
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "2":
            if p.money >= 250 and p.snowkingdompass != 1:
                p.money -= 250
                p.snowkingdompass = 1
            elif p.snowkingdompass == 1:
                print("---")
                print("This travel pass is already purchased.")
            else:
                print("---")
                print("Not enough money.")
            rpcshopupdate(p)
        if n == "3":
            break
    consoleClear()
    saveProcess(p, saves, lastsavepath)