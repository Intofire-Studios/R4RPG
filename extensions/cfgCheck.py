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
            config.getint("INVENTORY", "stone")
        except NoSectionError:
            config.add_section("INVENTORY")
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