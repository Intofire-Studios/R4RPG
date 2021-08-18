from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcshopupdate

def menu_passes(p):
    cfgsave(p, 'saves.ini')
    rpcshopupdate(p)
    consoleClear()
    while p.money > 0:
        cfgsave(p, 'saves.ini')
        print("---")
        print("Choose passes! Money: {}".format(p.money))
        print("---")
        if p.sandspass == 0:
            print("[COST: 100] 1. Sands pass")
        else:
            print("[PURCHASED] 1. Sands pass")
        print("2. Exit to shop menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.money >= 100 and p.sandspass == 0:
                p.money -= 100
                p.sandspass = 1
                rpcshopupdate(p)
            elif p.sandspass == 1:
                print("---")
                print("This travel pass is already purchased.")
                rpcshopupdate(p)
            else:
                print("---")
                print("Not enough money.")
                rpcshopupdate(p)
        if n == "2":
            break
    consoleClear()
    cfgsave(p, 'saves.ini')