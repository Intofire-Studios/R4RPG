from modules.menu_inventory import menu_inventory
from modules.menu_mine import menu_mine
from modules.menu_location import menu_location
from modules.menu_upgrade import menu_upgrade
from modules.menu_stats import menu_stats
from modules.menu_fight import menu_fight
from modules.menu_craft import menu_craft
from modules.menu_shop import menu_shop
from modules.menu_settings import menu_settings
from extensions.langSelect import lang
from extensions.richPresence import rpcupdate
from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath
from extensions.versionChecker import versionChecker, updaterChecker
from extensions.dlala import dlala
import os, time
import requests

def mainmenu(p):
    while True:
        saveProcess(p, saves, lastsavepath)
        lastsave = os.path.getmtime(saves)
        updaterChecker()
        consoleClear()
        rpcupdate(p)
        if versionChecker() == 1:
            print("---")
            print(lang['newversion'] + ' ' + lang['isavailable'] + ' — https://github.com/Intofire-Studios/R4RPG/releases')
            print('')
            info = requests.get('https://raw.githubusercontent.com/Intofire-Studios/R4RPG/master/extensions/version.txt')
            with open('extensions/version.txt', 'r') as f:
                print(lang['currentversion'] + f': {f.read()[9:-1]}')
            print(lang['newversion'] + f': {str(info.content)[11:-3]}')
        elif versionChecker() == 2:
            print("---")
            with open('extensions/version.txt', 'r') as f:
                print(f'v{f.read()[9:-1]} beta.')
        print("---")
        print(lang['choosemain'] + '!')
        print("---")
        if versionChecker() == 1:
            print('0. ' + lang['dwnldupd'])
        print("1. " + lang['fight'] + '!')
        if p.max_pickaxe != 0:
            print("2. " + lang['mine'] + '!' + " | " + lang['pickaxe'] + f": {p.pickaxe}/{p.max_pickaxe}")
        else:
            print("2. <" + lang['closed'] + ">")
        print("3. " + lang['stats'] + " | " + lang['hp'] + f": {p.hp}/{p.max_hp} | " + lang['power'] + f": {p.pw}")
        print("4. " + lang['inventory'])
        if p.sp > 0:
            print("5. " + lang['upgrade'] + " | " + lang['skillpoints'] + f": {p.sp}")
        else:
            print("5. <" + lang['closed'] + ">")
        print("6. " + lang['shop'] + " | " + lang['money'] + f": {p.money}")
        if p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0:
            print("7. " + lang['craft'])
        else:
            print("7. <" + lang['closed'] + ">")
        print("8. " + lang['location'] + " | " + lang['currentlocation'] + f": {p.location.capitalize()}")
        print("9. " + lang['settings'])
        print("10. " + lang['close'] + " | " + lang['lastsave'] + f": {time.ctime(lastsave)}")
        n = input(lang['number'] + ": ")
        if n == '0' and versionChecker() == 1:
            os.system('python updater/updater.py')
            exit()
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
            menu_craft(p)
        if n == "8":
            menu_location(p)
        if n == "9":
            menu_settings(p)
        if n == "10":
            consoleClear()
            print(lang['closing'] + "...")
            saveProcess(p, saves, lastsavepath)
            time.sleep(3)
            consoleClear()
            exit()
        #if n.lower() == "dlala":
        #    dlala(p)