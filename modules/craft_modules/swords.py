from extensions.cmdClear import consoleClear
from extensions.saveProcess import saveProcess
from extensions.richPresence import rpccraftupdate
from extensions.fileAssociation import saves, lastsavepath

def craft_swords(p):
    saveProcess(p, saves, lastsavepath)
    rpccraftupdate(p)
    consoleClear()
    while p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0:
        saveProcess(p, saves, lastsavepath)
        print("---")
        print(f"Choose what to craft! Resources: {p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver}")
        print("---")
        print("1. Stone sword       (Damage: 5)      [Stone: 4]")
        print("2. Silver sword      (Damage: 15)     [Silver: 6]")
        print("3. Iron sword        (Damage: 20)     [Iron: 8]")
        print("4. Gold sword        (Damage: 25)     [Gold: 10]")
        print("5. Emerald sword     (Damage: 40)     [Emerald: 14]")
        print("6. Diamond sword     (Damage: 50)     [Diamond: 20]")
        print("7. Exit to main menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            if p.stone >= 4:
                p.stone -= 4
                p.damage = 5
                p.sword, p.max_sword = 5, 5
            else:
                print("---")
                print("Not enough stone.")
            rpccraftupdate(p)
        if n == "2":
            if p.silver >= 6:
                p.silver -= 6
                p.damage = 15
                p.sword, p.max_sword = 15, 15
            else:
                print("---")
                print("Not enough silver.")
            rpccraftupdate(p)
        if n == "3":
            if p.iron >= 8:
                p.iron -= 8
                p.damage = 20
                p.sword, p.max_sword = 20, 20
            else:
                print("---")
                print("Not enough iron.")
            rpccraftupdate(p)
        if n == "4":
            if p.gold >= 10:
                p.gold -= 10
                p.damage = 25
                p.sword, p.max_sword = 25, 25
            else:
                print("---")
                print("Not enough gold.")
            rpccraftupdate(p)
        if n == "5":
            if p.emerald >= 14:
                p.emerald -= 14
                p.damage = 40
                p.sword, p.max_sword = 40, 40
            else:
                print("---")
                print("Not enough emerald.")
            rpccraftupdate(p)
        if n == "6":
            if p.diamond >= 20:
                p.diamond -= 20
                p.damage = 50
                p.sword, p.max_sword = 50, 50
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