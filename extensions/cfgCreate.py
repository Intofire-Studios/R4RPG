from configparser import ConfigParser

config = ConfigParser()
path = "saves.ini"

def cfgcreate(path):
    d = 0
    config.add_section("SAVE")
    config.set("SAVE", "name", input("Enter your name: "))
    config.set("SAVE", "discordstatus", input("Enable Discord Rich Presence? (Yes or No): ").lower())
    while d != 1:
        cls = input("Enter desired character class (Heavy, Medic or Warrior): ")
        if cls.lower() == "heavy":
            config.set("SAVE", "cls", "Heavy")
            config.set("SAVE", "hp", "25")
            config.set("SAVE", "max_hp", "25")
            config.set("SAVE", "heal_hp", "5")
            config.set("SAVE", "pw", "2")
            d = 1
        elif cls.lower() == "medic":
            config.set("SAVE", "cls", "Medic")
            config.set("SAVE", "hp", "10")
            config.set("SAVE", "max_hp", "10")
            config.set("SAVE", "heal_hp", "15")
            config.set("SAVE", "pw", "2")
            d = 1
        elif cls.lower() == "warrior":
            config.set("SAVE", "cls", "Warrior")
            config.set("SAVE", "hp", "10")
            config.set("SAVE", "max_hp", "10")
            config.set("SAVE", "heal_hp", "5")
            config.set("SAVE", "pw", "6")
            d = 1
        else:
            d = 0
    config.set("SAVE", "level", "1")
    config.set("SAVE", "sp", "0")
    config.set("SAVE", "money", "0")
    config.set("SAVE", "xp", "0")
    config.set("SAVE", "plus_pw", "1")
    config.set("SAVE", "max_xp", "5")
    config.set("SAVE", "pwpotion", "0")
    config.set("SAVE", "hppotion", "10")
    with open(path, "w+") as config_file:
        path = "saves.ini"
        config.write(config_file)