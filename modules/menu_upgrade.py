from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcupgradeupdate
from extensions.fileAssociation import saves, lastsavepath

def menu_upgrade(p):
    while p.sp > 0:
        saveProcess(p, saves, lastsavepath)
        rpcupgradeupdate(p)
        consoleClear()
        print("---")
        print(f"Choose your upgrades! Skill points: {p.sp}")
        print("---")
        print(f"1. HP: {p.hp}/{p.max_hp}")
        print(f"2. Power: {p.pw}")
        print(f"3. Heal potions power: {p.heal_hp}")
        print(f"4. Power potions power: {p.plus_pw}")
        print("5. Exit to main menu")
        n = input("Number: ")
        if n == "1":
            p.hp += 5
            p.sp -= 1
            p.max_hp += 5
            rpcupgradeupdate(p)
        if n == "2":
            p.pw += 1
            p.sp -= 1
            rpcupgradeupdate(p)
        if n == "3":
            p.heal_hp += 1
            p.sp -= 1
            rpcupgradeupdate(p)
        if n == "4":
            p.plus_pw += 1
            p.sp -= 1
            rpcupgradeupdate(p)
        if n == "5":
            break
        consoleClear()
    consoleClear()
    saveProcess(p, saves, lastsavepath)