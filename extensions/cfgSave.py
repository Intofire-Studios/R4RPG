from configparser import ConfigParser

config = ConfigParser()

def cfgsave(p, path):
    config.read(path)
    config.set("SAVE", "name", p.name)
    config.set("SAVE", "cls", p.cls)
    config.set("SAVE", "hp", str(p.hp))
    config.set("SAVE", "max_hp", str(p.max_hp))
    config.set("SAVE", "pw", str(p.pw))
    config.set("SAVE", "level", str(p.level))
    config.set("SAVE", "sp", str(p.sp))
    config.set("SAVE", "money", str(p.money))
    config.set("SAVE", "xp", str(p.xp))
    config.set("SAVE", "max_xp", str(p.max_xp))
    config.set("SAVE", "heal_hp", str(p.heal_hp))
    config.set("SAVE", "plus_pw", str(p.plus_pw))
    config.set("SAVE", "pwpotion", str(p.pwpotion))
    config.set("SAVE", "hppotion", str(p.hppotion))
    config.set("SAVE", "location", p.location)
    config.set("SAVE", "sandspass", str(p.sandspass))
    config.set("SAVE", "snowkingdompass", str(p.snowkingdompass))
    config.set("INVENTORY", "pickaxe", str(p.pickaxe))
    config.set("INVENTORY", "max_pickaxe", str(p.max_pickaxe))
    config.set("INVENTORY", "stone", str(p.stone))
    with open(path, "w") as config_file:
        config.write(config_file)
    config_file.close()