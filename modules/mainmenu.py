from modules.menu_inventory import menu_inventory
from modules.menu_mine import menu_mine
from modules.menu_location import menu_location
from extensions.richPresence import rpcupdate
from modules.menu_upgrade import menu_upgrade
from modules.menu_stats import menu_stats
from modules.menu_fight import menu_fight
from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves
from modules.menu_shop import menu_shop
import os.path, time

def mainmenu(p):
    while True:
        lastsave = os.path.getmtime(saves)
        consoleClear()
        rpcupdate(p)
        print("---")
        print("Choose what to do!")
        print("---")
        print("1. Go fight!")
        if p.max_pickaxe != 0:
            print("2. Go to the mine!        | Pickaxe: {}/{}".format(p.pickaxe, p.max_pickaxe))
        else:
            print("2. <CLOSED>")
        print("3. Check your stats       | HP: {}/{} | Power: {}".format(p.hp, p.max_hp, p.pw))
        print("4. Check your inventory")
        if p.sp > 0:
            print("5. Upgrade your character | Skill Points: {}".format(p.sp))
        else:
            print("5. <CLOSED>")
        if p.money > 0:
            print("6. Open shop              | Money: {}".format(p.money))
        else:
            print("6. <CLOSED>")
        print("7. Change your location   | Current location: {}".format(p.location.capitalize()))
        print("8. Close the game         | Last save: {}".format(time.ctime(lastsave)))
        n = input("Number: ")
        if n == "1":
            menu_fight(p)
        if n == "2":
            menu_mine(p)
        if n == "3":
            menu_stats(p)
        if n == "4":
            menu_inventory(p)
        if n == "5":
            menu_upgrade(p)
        if n == "6":
            menu_shop(p)
        if n == "7":
            menu_location(p)
        if n == "8":
            consoleClear()
            print("Closing the game...")
            cfgsave(p, saves)
            time.sleep(3)
            exit()
