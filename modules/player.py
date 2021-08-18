from configparser import ConfigParser

config = ConfigParser()
config.read("saves.ini")

class Player:
    name = config.get("SAVE", "name")
    cls = config.get("SAVE", "cls")
    hp = config.getint("SAVE", "hp")
    max_hp = config.getint("SAVE", "max_hp")
    pw = config.getint("SAVE", "pw")
    level = config.getint("SAVE", "level")
    sp = config.getint("SAVE", "sp")
    money = config.getint("SAVE", "money")
    xp = config.getint("SAVE", "xp")
    max_xp = config.getint("SAVE", "max_xp")
    heal_hp = config.getint("SAVE", "heal_hp")
    plus_pw = config.getint("SAVE", "plus_pw")
    pwpotion = config.getint("SAVE", "pwpotion")
    hppotion = config.getint("SAVE", "hppotion")