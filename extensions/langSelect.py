from configparser import ConfigParser
import sqlite3

config = ConfigParser()
connection = sqlite3.connect('settings.sqlite')
cursor = connection.cursor()

cursor.execute("SELECT * FROM settings;")
section = cursor.fetchone()[1].upper()
config.read(f"locales/{section.lower()}.ini")

lang = {
    # modules/mainmenu.py
    'newversion': config.get(section, "newversion").encode('cp1251').decode('utf-8'),
    'currentversion': config.get(section, "currentversion").encode('cp1251').decode('utf-8'),
    'isavailable': config.get(section, "isavailable").encode('cp1251').decode('utf-8'),
    'choosemain': config.get(section, "choosemain").encode('cp1251').decode('utf-8'),
    'dwnldupd': config.get(section, "dwnldupd").encode('cp1251').decode('utf-8'),
    'fight': config.get(section, "fight").encode('cp1251').decode('utf-8'),
    'mine': config.get(section, "mine").encode('cp1251').decode('utf-8'),
    'pickaxe': config.get(section, "pickaxe").encode('cp1251').decode('utf-8'),
    'closed': config.get(section, "closed").encode('cp1251').decode('utf-8'),
    'menustats': config.get(section, "menustats").encode('cp1251').decode('utf-8'),
    'hp': config.get(section, "hp").encode('cp1251').decode('utf-8'),
    'power': config.get(section, "power").encode('cp1251').decode('utf-8'),
    'inventory': config.get(section, "inventory").encode('cp1251').decode('utf-8'),
    'upgrade': config.get(section, "upgrade").encode('cp1251').decode('utf-8'),
    'skillpoints': config.get(section, "skillpoints").encode('cp1251').decode('utf-8'),
    'shop': config.get(section, "shop").encode('cp1251').decode('utf-8'),
    'money': config.get(section, "money").encode('cp1251').decode('utf-8'),
    'craft': config.get(section, "craft").encode('cp1251').decode('utf-8'),
    'location': config.get(section, "location").encode('cp1251').decode('utf-8'),
    'currentlocation': config.get(section, "currentlocation").encode('cp1251').decode('utf-8'),
    'settings': config.get(section, "settings").encode('cp1251').decode('utf-8'),
    'close': config.get(section, "close").encode('cp1251').decode('utf-8'),
    'lastsave': config.get(section, "lastsave").encode('cp1251').decode('utf-8'),
    'number': config.get(section, "number").encode('cp1251').decode('utf-8'),
    'closing': config.get(section, "closing").encode('cp1251').decode('utf-8'),

    # modules/menu_settings.py
    'changelang': config.get(section, "changelang").encode('cp1251').decode('utf-8'),
    'exittomain': config.get(section, "exittomain").encode('cp1251').decode('utf-8'),
    'newlang': config.get(section, "newlang").encode('cp1251').decode('utf-8'),
    
    # modules/menu_location.py
    'chooselocation': config.get(section, "chooselocation").encode('cp1251').decode('utf-8'),
    'spawn': config.get(section, "spawn").encode('cp1251').decode('utf-8'),
    'sands': config.get(section, "sands").encode('cp1251').decode('utf-8'),
    'snowkingdom': config.get(section, "snowkingdom").encode('cp1251').decode('utf-8'),
    
    # modules/menu_stats.py
    'stats': config.get(section, "stats").encode('cp1251').decode('utf-8'),
    'name': config.get(section, "name").encode('cp1251').decode('utf-8'),
    'cls': config.get(section, "cls").encode('cp1251').decode('utf-8'),
    'lvl': config.get(section, "lvl").encode('cp1251').decode('utf-8'),
    'xp': config.get(section, "xp").encode('cp1251').decode('utf-8'),
    'healing': config.get(section, "healing").encode('cp1251').decode('utf-8'),
    'pwrboost': config.get(section, "pwrboost").encode('cp1251').decode('utf-8'),
    'pwpotions': config.get(section, "pwpotions").encode('cp1251').decode('utf-8'),
    'healpotions': config.get(section, "healpotions").encode('cp1251').decode('utf-8'),
    'travelpasses': config.get(section, "travelpasses").encode('cp1251').decode('utf-8'),
    'spawnpass': config.get(section, "spawnpass").encode('cp1251').decode('utf-8'),
    'sandspass': config.get(section, "sandspass").encode('cp1251').decode('utf-8'),
    'snowkingdompass': config.get(section, "spawnpass").encode('cp1251').decode('utf-8'),
    'ntrtocontinue': config.get(section, "ntrtocontinue").encode('cp1251').decode('utf-8'),
    
}

connection.close()