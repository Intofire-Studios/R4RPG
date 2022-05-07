from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath, settingspath
from extensions.saveProcess import saveProcess
from extensions.settingsCreate import settingsCreate
from extensions.langSelect import lang
import os
from time import sleep

def menu_settings(p):
    saveProcess(p, saves, lastsavepath)
    consoleClear()
    while True:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(lang['choosemain'] + "!")
        print("---")
        print("1. Change language")
        print("2. Exit to main menu")
        n = input(lang['number'] + ": ")
        consoleClear()
        if n == "1":
            os.remove(settingspath)
            settingsCreate(settingspath)
            consoleClear()
            print("The new language will be active after restarting the game")
            sleep(3)
            break
        if n == "2":
            break