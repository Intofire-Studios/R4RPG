from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from random import randint, choice
from modules.menu_upgrade import menu_upgrade
from extensions.richPresence import rpclose, rpcupdate, rpcfightupdate
from extensions.fileAssociation import saves
from modules import enemies
from time import sleep
from math import ceil

def menu_fight(p):  # sourcery no-metrics
    cfgsave(p, saves)
    usedpwpotions = 0
    rpcfightupdate(p)

    if p.location == "spawn":
        enemy = choice(enemies.enemyspawn)

        if enemy in enemies.enemyspawnregular:
            ehp = randint(10,20) + ceil(p.max_hp * 0.33)
            epw = 2 * randint(1,5) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemyspawnnormal:
            ehp = randint(30,50) + ceil(p.max_hp * 0.33)
            epw = 2 * randint(3,7) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemyspawnboss:
            ehp = randint(75,100) + ceil(p.max_hp * 0.33)
            epw = 2 * randint(5,10) + ceil(p.pw * 0.25)
    elif p.location == "sands":
        enemy = choice(enemies.enemysands)

        if enemy in enemies.enemysandsregular:
            ehp = randint(30,50) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(2,10) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemysandsnormal:
            ehp = randint(55,95) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(4,12) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemysandsboss:
            ehp = randint(100,130) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(10,20) + ceil(p.pw * 0.5)
    elif p.location == "snow kingdom":
        enemy = choice(enemies.enemysnowkingdom)

        if enemy in enemies.enemysnowkingdomregular:
            ehp = randint(40,60) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(4,15) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemysnowkingdomnormal:
            ehp = randint(70,100) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(6,20) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemysnowkingdomboss:
            ehp = randint(120,150) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(15,30) + ceil(p.pw * 0.5)

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
            r = randint(1,4)
            if r == 3:
                consoleClear()
                print("---")
                print("You ran away!")
                print("---")
                sleep(3)
                return True
            else:
                consoleClear()
                print("---")
                print("You can't run!")
            rpcfightupdate(p)
    if usedpwpotions != 0:
        p.pw -= usedpwpotions * p.plus_pw
    rpcupdate(p)

    if p.location == "spawn":
        p.xp += 1
    elif p.location == "sands":
        p.xp += 3
    elif p.location == "snow kingdom":
        p.xp += 5
    p.sp += 1
    p.money += 1

    r = randint(1, 100)
    if r == 100 and p.sandspass == 0 and p.location == "spawn":
        p.sandspass = 1
    
    ch = randint(1, 250)
    if ch == 250 and p.snowkingdompass == 0 and p.location == "sands":
        p.snowkingdompass = 1

    cfgsave(p, saves)
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1
        p.sp += 2
        menu_upgrade(p)