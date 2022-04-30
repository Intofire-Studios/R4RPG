from extensions.cmdClear import consoleClear
from extensions.saveProcess import saveProcess
from extensions.richPresence import rpccraftupdate
from extensions.fileAssociation import saves, lastsavepath

def craft_armor(p):
    saveProcess(p, saves, lastsavepath)
    rpccraftupdate(p)
    consoleClear()
    while p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(f"Choose what to craft! Resources: {p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver}")
        print("---")
        print("1. Stone armor       (Strength: 5)      [Stone: 3]")
        print("2. Silver armor      (Strength: 15)     [Silver: 5]")
        print("3. Iron armor        (Strength: 20)     [Iron: 7]")
        print("4. Gold armor        (Strength: 25)     [Gold: 11]")
        print("5. Emerald armor     (Strength: 40)     [Emerald: 16]")
        print("6. Diamond armor     (Strength: 50)     [Diamond: 25]")
        print("7. Exit to main menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.stone >= 3:
                p.stone -= 3
                p.armor, p.max_armor = 5, 5
            else:
                print("---")
                print("Not enough stone.")
            rpccraftupdate(p)
        if n == "2":
            if p.silver >= 5:
                p.silver -= 5
                p.armor, p.max_armor = 15, 15
            else:
                print("---")
                print("Not enough silver.")
            rpccraftupdate(p)
        if n == "3":
            if p.iron >= 7:
                p.iron -= 7
                p.armor, p.max_armor = 20, 20
            else:
                print("---")
                print("Not enough iron.")
            rpccraftupdate(p)
        if n == "4":
            if p.gold >= 11:
                p.gold -= 11
                p.armor, p.max_armor = 25, 25
            else:
                print("---")
                print("Not enough gold.")
            rpccraftupdate(p)
        if n == "5":
            if p.emerald >= 16:
                p.emerald -= 16
                p.armor, p.max_armor = 40, 40
            else:
                print("---")
                print("Not enough emerald.")
            rpccraftupdate(p)
        if n == "6":
            if p.diamond >= 25:
                p.diamond -= 25
                p.armor, p.max_armor = 50, 50
            else:
                print("---")
                print("Not enough diamond.")
            rpccraftupdate(p)
        if n == "7":
            rpccraftupdate(p)
            break
        rpccraftupdate(p)
    consoleClear()
    saveProcess(p, saves, lastsavepath)