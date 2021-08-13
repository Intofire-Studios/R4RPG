def menu_stats(p):
    print("---")
    print("Player stats!")
    print("---")
    print("HP: {}/{}".format(p.hp,p.max_hp))
    print("Healing {}".format(p.heal_hp))
    print("Power {}".format(p.pw))
    input("Enter to continue.")