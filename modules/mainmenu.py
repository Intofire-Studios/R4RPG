from extensions.richPresence import rpcupdate
from modules.menu_upgrade import menu_upgrade
from time import sleep
from modules.menu_stats import menu_stats
from modules.menu_fight import menu_fight
from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from modules.menu_shop import menu_shop

def mainmenu(p):
    while True:
        consoleClear()
        rpcupdate(p)
        print("---")
        print("Choose what to do")
        print("---")
        print("1. Go fight!")
        print("2. Check your stats")
        if p.sp > 0:
            print("3. Upgrade your character | Skill Points: {}".format(p.sp))
        else:
            print("3. <CLOSED>")
        if p.money > 0:
            print("4. Open shop              | Money: {}".format(p.money))
        else:
            print("4. <CLOSED>")
        print("5. Close the game")
        n = input("Number: ")
        if n == "1":
            menu_fight(p)
        if n == "2":
            menu_stats(p)
        if n == "3":
            menu_upgrade(p)
        if n == "4":
            menu_shop(p)
        if n == "5":
            print("Closing the game...")
            cfgsave(p, 'saves.ini')
            sleep(3)
            exit()
