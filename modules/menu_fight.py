from extensions.cmdClear import consoleClear
from random import randint, choice
from modules.menu_upgrade import menu_upgrade as menu_upgrade
from modules import enemies
from time import sleep

def menu_fight(p):
    ehp = 5 * randint(4,20)
    epw = 2 * randint(1,5)
    enemy = choice(enemies.enemy).capitalize()
    consoleClear()
    while ehp > 0:
        print("---")
        print("{}: {}. Power: {}".format(enemy, ehp, epw))
        print("{}: {}/{}. Power: {}".format(p.name, p.hp,p.max_hp, p.pw))
        print("---")
        print("1. Punch with power {}".format(p.pw))
        print("2. Heal (+{})".format(p.heal_hp))
        print("3. Run away!")
        n = input("Number: ")
        if n == "1":
            r = randint(1,2)
            if r == 1:
                ehp -= p.pw
                consoleClear()
                print("---")
                print("You hit the enemy!")
            if r == 2:
                p.hp -= epw
                consoleClear()
                print("---")
                print("Enemy hit you!")
                if p.hp <= 0:
                    consoleClear()
                    print("---")
                    print("You've lost!")
                    print("---")
                    sleep(5)
                    exit()
        if n == "2":
            p.hp += p.heal_hp
            if p.hp > p.max_hp:
                p.hp = p.max_hp
            consoleClear()
            print("---")
            print("Healing... {}".format(p.hp))
        if n == "3":
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
    p.xp += 1
    p.sp += 1
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1
        p.sp += 2
        menu_upgrade(p)