from configparser import ConfigParser, NoOptionError, NoSectionError
import os
config = ConfigParser()

def cfgcheck(path):
    config.read(path)
    if os.path.exists(path):
        try:
            config.get("SAVE", "location")
        except NoOptionError:
            config.set("SAVE", "location", "spawn")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()    

        try:
            config.getint("SAVE", "sandspass")
        except NoOptionError:
            config.set("SAVE", "sandspass", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("SAVE", "snowkingdompass")
        except NoOptionError:
            config.set("SAVE", "snowkingdompass", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()
        
        try:
            config.getint("INVENTORY", "pickaxe")
        except NoSectionError:
            config.add_section("INVENTORY")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "pickaxe")
        except NoOptionError:
            config.set("INVENTORY", "pickaxe", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "max_pickaxe")
        except NoOptionError:
            config.set("INVENTORY", "max_pickaxe", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "stone")
        except NoOptionError:
            config.set("INVENTORY", "stone", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "copper")
        except NoOptionError:
            config.set("INVENTORY", "copper", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "tin")
        except NoOptionError:
            config.set("INVENTORY", "tin", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "iron")
        except NoOptionError:
            config.set("INVENTORY", "iron", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "aluminum")
        except NoOptionError:
            config.set("INVENTORY", "aluminum", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()
        
        try:
            config.getint("INVENTORY", "silver")
        except NoOptionError:
            config.set("INVENTORY", "silver", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "topaz")
        except NoOptionError:
            config.set("INVENTORY", "topaz", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "gold")
        except NoOptionError:
            config.set("INVENTORY", "gold", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "crystal")
        except NoOptionError:
            config.set("INVENTORY", "crystal", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "diamond")
        except NoOptionError:
            config.set("INVENTORY", "diamond", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "ruby")
        except NoOptionError:
            config.set("INVENTORY", "ruby", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()

        try:
            config.getint("INVENTORY", "emerald")
        except NoOptionError:
            config.set("INVENTORY", "emerald", "0")
            with open(path, "w+") as config_file:
                config.write(config_file)
            config_file.close()