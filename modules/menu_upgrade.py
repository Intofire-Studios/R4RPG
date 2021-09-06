from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcupgradeupdate

def menu_upgrade(p):
    while p.sp > 0:
        cfgsave(p, 'saves.ini')
        rpcupgradeupdate(p)
        consoleClear()
        print("---")
        print("Choose your upgrades! Skill points: {}".format(p.sp))
        print("---")
        print("1. HP: {}/{}".format(p.hp, p.max_hp))
        print("2. Power: {}".format(p.pw))
        print("3. Heal potions power: {}".format(p.heal_hp))
        print("4. Power potions power: {}".format(p.plus_pw))
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
    cfgsave(p, 'saves.ini')