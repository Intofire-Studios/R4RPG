from configparser import ConfigParser
from extensions import cmdClear
import os
config = ConfigParser()

def cfgcreate(path):
    if os.path.exists(path):
        return
    d = 0
    cmdClear.consoleClear()
    config.add_section("SAVE")
    config.set("SAVE", "name", input("Enter your name: "))
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
    config.set("SAVE", "location", "spawn")
    config.set("SAVE", "sandspass", "0")
    config.set("SAVE", "snowkingdompass", "0")
    config.add_section("INVENTORY")
    config.set("INVENTORY", "pickaxe", "0")
    config.set("INVENTORY", "max_pickaxe", "0")
    config.set("INVENTORY", "stone", "0")
    config.set("INVENTORY", "copper", "0")
    config.set("INVENTORY", "tin", "0")
    config.set("INVENTORY", "iron", "0")
    config.set("INVENTORY", "aluminum", "0")
    config.set("INVENTORY", "silver", "0")
    config.set("INVENTORY", "topaz", "0")
    config.set("INVENTORY", "gold", "0")
    config.set("INVENTORY", "crystal", "0")
    config.set("INVENTORY", "diamond", "0")
    config.set("INVENTORY", "emerald", "0")
    config.set("INVENTORY", "emerald", "0")
    with open(path, "w+") as config_file:
        config.write(config_file)
    config_file.close()