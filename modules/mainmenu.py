from time import sleep
from modules.menu_stats import menu_stats as menu_stats
from modules.menu_fight import menu_fight as menu_fight
from extensions.cfgSave import cfgsave as cfgsave
from extensions.cmdClear import consoleClear as consoleClear

def mainmenu(p):
    consoleClear()
    while True:
        print("---")
        print("Choose what to do")
        print("1. Go fight!")
        print("2. Check your stats")
        print("3. Close the game")
        n = input("Number: ")
        if n == "1":
            menu_fight(p)
        if n == "2":
            menu_stats(p)
        if n == "3":
            print("Closing the game...")
            cfgsave(p, 'saves.ini')
            sleep(3)
            exit()