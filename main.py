from random import randint

class Player:
    hp = 10
    max_hp = 10
    pw = 2
    level = 1
    sp = 5
    xp = 0
    max_xp = 100
    heal_hp = 5

p = Player()

def menu_upgrade(p):
    while p.sp > 0:
        print("Choose your upgrades! Skill points: {}".format(p.sp))
        print("---")
        print("1. HP {}/{}".format(p.hp, p.max_hp))
        print("2. Power {}".format(p.pw))
        print("3. Heal points {}".format(p.heal_hp))
        n = input("Number: ")
        if n == "1":
            p.hp += 5
            p.sp -= 1
            p.max_hp += 5
        if n == "2":
            p.pw += 1
            p.sp -= 1
        if n == "3":
            p.heal_hp += 1
            p.sp -= 1

def menu_stats(p):
    print("Player stats!")
    print("---")
    print("HP: {}/{}".format(p.hp,p.max_hp))
    print("Healing {}".format(p.heal_hp))
    print("Power {}".format(p.pw))
    input("Enter to continue.")

def mainmenu(p):
    while True:
        print("Choose what to do")
        print("1. Go fight!")
        print("2. Check your stats")
        n = input("Number: ")
        if n == "1":
            menu_fight(p)
        if n == "2":
            menu_stats(p)

def menu_fight(p):
    ehp = 5 * randint(4,20)
    epw = 2 * randint(1,5)
    while ehp > 0:
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
                print("You hit the enemy!")
            if r == 2:
                p.hp -= epw
                print("Enemy hit you!")
                if p.hp < 0:
                    print("You loose!")
                    return False
        if n == "2":
            p.hp += p.heal_hp
            if p.hp > p.max_hp:
                p.hp = p.max_hp
            print("Healing... {}".format(p.hp))
        if n == "3":
            r = randint(1,3)
            if r == "3":
                print("You ran away!")
                return True
            else:
                print("You can't run!")
    p.xp += 1
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1
        menu_upgrade(p)

p = Player()
menu_upgrade(p)
mainmenu(p)
