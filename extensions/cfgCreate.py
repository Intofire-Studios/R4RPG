from configparser import ConfigParser

config = ConfigParser()
path = "saves.ini"

def cfgcreate(path):
    config.add_section("SAVE")
    config.set("SAVE", "name", input("Enter your name: "))
    config.set("SAVE", "hp", "10")
    config.set("SAVE", "max_hp", "10")
    config.set("SAVE", "pw", "2")
    config.set("SAVE", "level", "1")
    config.set("SAVE", "sp", "5")
    config.set("SAVE", "xp", "0")
    config.set("SAVE", "max_xp", "100")
    config.set("SAVE", "heal_hp", "5")
    with open(path, "w+") as config_file:
        path = "saves.ini"
        config.write(config_file)