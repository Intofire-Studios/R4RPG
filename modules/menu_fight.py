from extensions.cmdClear import consoleClear
from random import randint, choice
from modules.menu_upgrade import menu_upgrade
from extensions.richPresence import rpclose, rpcupdate, rpcfightupdate
from modules import enemies
from time import sleep
from math import ceil

def menu_fight(p):
    usedpwpotions = 0
    rpcfightupdate(p)
    ehp = 5 * randint(4,20) + ceil(p.max_hp * 0.25)
    epw = 2 * randint(1,5) + ceil(p.pw * 0.25)
    enemy = choice(enemies.enemy).capitalize()
    consoleClear()
    while ehp > 0:
        print("---")
        print("{}: {}. Power: {}".format(enemy, ehp, epw))
        print("{}: {}/{}. Power: {}".format(p.name, p.hp,p.max_hp, p.pw))
        print("---")
        print("1. Punch with power {}".format(p.pw))
        print("2. Use heal potion (+{}) ({} left)".format(p.heal_hp, p.hppotion))
        print("3. Use power potion ({} left)".format(p.pwpotion))
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
                p.pw += 5
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
        p.pw -= usedpwpotions*5
    rpcupdate(p)
    p.xp += 1
    p.sp += 1
    p.money += 1
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1
        p.sp += 2
        menu_upgrade(p)