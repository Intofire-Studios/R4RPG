from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from random import randint, choice
from modules.menu_upgrade import menu_upgrade
from extensions.richPresence import rpclose, rpcupdate, rpcfightupdate
from modules import enemies
from time import sleep
from math import ceil

def menu_fight(p):
    cfgsave(p, 'saves.ini')
    usedpwpotions = 0
    rpcfightupdate(p)

    if p.location == "spawn":
        enemy = choice(enemies.enemyspawn)

        if enemy in enemies.enemyspawnregular:
            ehp = randint(10,20) + ceil(p.max_hp * 0.25)
            epw = 2 * randint(1,5) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemyspawnnormal:
            ehp = randint(30,50) + ceil(p.max_hp * 0.25)
            epw = 2 * randint(3,7) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemyspawnboss:
            ehp = randint(75,100) + ceil(p.max_hp * 0.25)
            epw = 2 * randint(5,10) + ceil(p.pw * 0.25)
    elif p.location == "sands":
        enemy = choice(enemies.enemysands)

        if enemy in enemies.enemysandsregular:
            ehp = randint(10,20) + ceil(p.max_hp * 0.25)
            epw = 2 * randint(1,5) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemysandsnormal:
            ehp = randint(30,50) + ceil(p.max_hp * 0.25)
            epw = 2 * randint(3,7) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemysandsboss:
            ehp = randint(75,100) + ceil(p.max_hp * 0.25)
            epw = 2 * randint(5,10) + ceil(p.pw * 0.25)

    enemy = enemy.capitalize()

    consoleClear()
    while ehp > 0:
        print("---")
        print("{}: {}. Power: {}".format(enemy, ehp, epw))
        print("{}: {}/{}. Power: {}".format(p.name, p.hp,p.max_hp, p.pw))
        print("---")
        print("1. Punch with power {}".format(p.pw))
        print("2. Use heal potion (+{}) ({} left)".format(p.heal_hp, p.hppotion))
        print("3. Use power potion (+{}) ({} left)".format(p.plus_pw, p.pwpotion))
        print("4. Run away!")
        n = input("Number: ")
        if n == "1":
            r = randint(1,2)
            if r == 1:
                ehp -= p.pw
                consoleClear()
                print("---")
                print("You hit the enemy!")
                rpcfightupdate(p)
            if r == 2:
                p.hp -= epw
                consoleClear()
                print("---")
                print("Enemy hit you!")
                rpcfightupdate(p)
                if p.hp <= 0:
                    consoleClear()
                    print("---")
                    print("You've lost!")
                    print("---")
                    rpclose(p)
                    sleep(5)
                    exit()
        if n == "2":
            consoleClear()
            if p.hppotion > 0:
                consoleClear()
                p.hppotion -= 1
                p.hp += p.heal_hp
                if p.hp > p.max_hp:
                    p.hp = p.max_hp
                consoleClear()
                print("---")
                print("Healing... {}".format(p.hp))
                rpcfightupdate(p)
            else:
                print("---")
                print("Not enough potions!")
        if n == "3":
            consoleClear()
            if p.pwpotion > 0:
                consoleClear()
                usedpwpotions += 1
                p.pwpotion -= 1
                p.pw += p.plus_pw
                print("---")
                print("Drinking the potion... {}".format(p.pw))
                rpcfightupdate(p)
            else:
                print("---")
                print("Not enough potions!")
        if n == "4":
            r = randint(1,3)
            if r == "3":
                consoleClear()
                print("---")
                print("You ran away!")
                return True
            else:
                consoleClear()
                print("---")
                print("You can't run!")
            rpcfightupdate(p)
    if usedpwpotions != 0:
        p.pw -= usedpwpotions * p.plus_pw
    rpcupdate(p)
    p.xp += 1
    p.sp += 1
    p.money += 1

    r = randint(1, 100)
    if r == 100 and p.sandspass == 0 and p.location == "spawn":
        p.sandspass = 1

    cfgsave(p, 'saves.ini')
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1
        p.sp += 2
        menu_upgrade(p)