from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcupgradeupdate
from extensions.fileAssociation import saves, lastsavepath
from extensions.langSelect import lang

def menu_upgrade(p):
    while p.sp > 0:
        saveProcess(p, saves, lastsavepath)
        rpcupgradeupdate(p)
        consoleClear()
        print("---")
        print(lang['upgrades'] + "! " + lang['skillpoints'] + f": {p.sp}")
        print("---")
        print("1. " + lang['hp'] + f": {p.hp}/{p.max_hp}")
        print("2. " + lang['power'] + f": {p.pw}")
        print("3. " + lang['hppower'] + f": {p.heal_hp}")
        print("4. " + lang['pppower'] + f": {p.plus_pw}")
        print("5. " + lang['exittomain'])
        n = input(lang['number'] + ": ")
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