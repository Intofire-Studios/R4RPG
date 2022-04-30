from modules.shop_pages.pickaxes import menu_pickaxes
from modules.shop_pages.passes import menu_passes
from modules.shop_pages.potions import menu_potions
from modules.shop_pages.resources.sell import menu_resources_sell
from modules.shop_pages.resources.buy import menu_resources_buy
from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcshopupdate
from extensions.fileAssociation import saves, lastsavepath

def menu_shop(p):
    saveProcess(p, saves, lastsavepath)
    rpcshopupdate(p)
    consoleClear()
    while True:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(f"Choose a category! Money: {p.money}")
        print("---")
        print("1. Potions")
        print("2. Travel passes")
        print("3. Pickaxes")
        print("4. Buy resources")
        print(f"5. Sell resources         | Resources: {p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver}")
        print("6. Exit to main menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            menu_potions(p)
        if n == "2":
            menu_passes(p)
        if n == "3":
            menu_pickaxes(p)
        if n == "4":
            menu_resources_buy(p)
        if n == "5":
            menu_resources_sell(p)
        if n == "6":
            break
    consoleClear()
    saveProcess(p, saves, lastsavepath)