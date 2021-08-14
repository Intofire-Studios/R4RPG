from configparser import ConfigParser

config = ConfigParser()
config.read("saves.ini")

class Player:
    name = config.get("SAVE", "name")
    cls = config.get("SAVE", "cls")
    hp = int(config.get("SAVE", "hp"))
    max_hp = int(config.get("SAVE", "max_hp"))
    pw = int(config.get("SAVE", "pw"))
    level = int(config.get("SAVE", "level"))
    sp = int(config.get("SAVE", "sp"))
    xp = int(config.get("SAVE", "xp"))
    max_xp = int(config.get("SAVE", "max_xp"))
    heal_hp = int(config.get("SAVE", "heal_hp"))