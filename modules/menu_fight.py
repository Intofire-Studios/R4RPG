from random import randint
from modules.menu_upgrade import menu_upgrade as menu_upgrade

def menu_fight(p):
    ehp = 5 * randint(4,20)
    epw = 2 * randint(1,5)
    while ehp > 0:
        print("---")
        print("ENEMY: {}. Power: {}".format(ehp, epw))
        print("YOU: {}/{}. Power: {}".format(p.hp,p.max_hp, p.pw))
        print("---")
        print("1. Punch with power {}".format(p.pw))
        print("2. Heal (+{})".format(p.heal_hp))
        print("3. Run away!")
        n = input("Number: ")
        if n == "1":
            r = randint(1,2)
            if r == 1:
                ehp -= p.pw
                print("---")
                print("You hit the enemy!")
            if r == 2:
                p.hp -= epw
                print("---")
                print("Enemy hit you!")
                if p.hp < 0:
                    print("---")
                    print("You loose!")
                    return False
        if n == "2":
            p.hp += p.heal_hp
            if p.hp > p.max_hp:
                p.hp = p.max_hp
            print("---")
            print("Healing... {}".format(p.hp))
        if n == "3":
            r = randint(1,3)
            if r == "3":
                print("---")
                print("You ran away!")
                return True
            else:
                print("---")
                print("You can't run!")
    p.xp += 1
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1
        menu_upgrade(p)