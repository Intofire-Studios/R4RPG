from extensions.cmdClear import consoleClear
from extensions.saveProcess import saveProcess
from extensions.richPresence import rpccraftupdate
from extensions.fileAssociation import saves, lastsavepath
from modules.craft_modules.armor import craft_armor
from modules.craft_modules.swords import craft_swords

def menu_craft(p):
    saveProcess(p, saves, lastsavepath)
    rpccraftupdate(p)
    consoleClear()
    while p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(f"Choose a category! Resources: {p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver}")
        print("---")
        print("1. Armor")
        print("2. Swords")
        print("3. Exit to main menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            craft_armor(p)
        if n == "2":
            craft_swords(p)
        if n == "3":
            break
    consoleClear()
    saveProcess(p, saves, lastsavepath)