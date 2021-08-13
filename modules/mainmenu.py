from time import sleep
from modules.menu_stats import menu_stats as menu_stats
from modules.menu_fight import menu_fight as menu_fight

def mainmenu(p):
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
            sleep(3)
            exit()