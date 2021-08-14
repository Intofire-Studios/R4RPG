from configparser import ConfigParser
from modules import player
import os

config = ConfigParser()

p = player.Player()

def cfgsave(p, path):
    os.remove(path)
    config.add_section("SAVE")
    config.set("SAVE", "name", p.name)
    config.set("SAVE", "cls", p.cls)
    config.set("SAVE", "hp", str(p.hp))
    config.set("SAVE", "max_hp", str(p.max_hp))
    config.set("SAVE", "pw", str(p.pw))
    config.set("SAVE", "level", str(p.level))
    config.set("SAVE", "sp", str(p.sp))
    config.set("SAVE", "xp", str(p.xp))
    config.set("SAVE", "max_xp", str(p.max_xp))
    config.set("SAVE", "heal_hp", str(p.heal_hp))
    with open(path, "w") as config_file:
        path = "saves.ini"
        config.write(config_file)