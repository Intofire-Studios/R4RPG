import sqlite3
from configparser import ConfigParser
from extensions import saveCreate
import os

def savePort(pathsave, path):
    oldpath = 'saves.ini'
    if os.path.exists(oldpath):
        connection = sqlite3.connect(path)
        config = ConfigParser()
        config.read(oldpath)

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
        location = config.get("SAVE", "location")
        sandspass = config.getint("SAVE", "sandspass")
        snowkingdompass = config.getint("SAVE", "snowkingdompass")

        pickaxe = config.getint("INVENTORY", "pickaxe")
        max_pickaxe = config.getint("INVENTORY", "max_pickaxe")
        stone = config.getint("INVENTORY", "stone")
        copper = config.getint("INVENTORY", "copper")
        tin = config.getint("INVENTORY", "tin")
        iron = config.getint("INVENTORY", "iron")
        aluminum = config.getint("INVENTORY", "aluminum")
        gold = config.getint("INVENTORY", "gold")
        crystal = config.getint("INVENTORY", "crystal")
        diamond = config.getint("INVENTORY", "diamond")
        emerald = config.getint("INVENTORY", "emerald")
        topaz = config.getint("INVENTORY", "topaz")
        ruby = config.getint("INVENTORY", "ruby")
        silver = config.getint("INVENTORY", "silver")

        newsave = open("saves.sqlite", "w+")
        newsave.close()

        create_save_table = """
                CREATE TABLE IF NOT EXISTS save (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cls TEXT NOT NULL,
                hp INTEGER,
                max_hp INTEGER,
                heal_hp INTEGER,
                pw INTEGER,
                level INTEGER,
                sp INTEGER,
                money INTEGER,
                xp INTEGER,
                plus_pw INTEGER,
                max_xp INTEGER,
                pwpotion INTEGER,
                hppotion INTEGER,
                location TEXT,
                sandspass INTEGER,
                snowkingdompass INTEGER
                );
                """
                
        create_inventory_table = """
            CREATE TABLE IF NOT EXISTS inventory(
            id INTEGER PRIMARY KEY, 
            pickaxe INTEGER,
            max_pickaxe INTEGER,
            stone INTEGER,
            copper INTEGER,
            tin INTEGER,
            iron INTEGER,
            aluminum INTEGER,
            silver INTEGER,
            topaz INTEGER,
            gold INTEGER,
            crystal INTEGER,
            diamond INTEGER,
            emerald INTEGER,
            ruby INTEGER
            );
            """
        saveCreate.execute_query(connection, create_save_table)
        saveCreate.execute_query(connection, create_inventory_table)

        create_save = """
            INSERT INTO
                save (id, name, cls, hp, max_hp, heal_hp, pw, level, sp, money, xp, plus_pw, max_xp, pwpotion, hppotion, location, sandspass, snowkingdompass)
            VALUES
                (1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        data = (name, cls, hp, max_hp, heal_hp, pw, level, sp, money, xp, plus_pw, max_xp, pwpotion, hppotion, location, sandspass, snowkingdompass)

        create_inventory = """
            INSERT INTO
                inventory (id, pickaxe, max_pickaxe, stone, copper, tin, iron, aluminum, silver, topaz, gold, crystal, diamond, emerald, ruby)
            VALUES
                (1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        data1 = (pickaxe, max_pickaxe, stone, copper, tin, iron, aluminum, silver, topaz, gold, crystal, diamond, emerald, ruby)

        connection.execute(create_save, data)
        connection.execute(create_inventory, data1)
        connection.commit()
        connection.close()

        os.remove(oldpath)
        
        realtime = os.path.getmtime(path)
        if not os.path.exists(pathsave):
            with open(pathsave, "w+") as newsave:
                newsave.write(str(realtime))
        else:
            os.remove(pathsave)
            with open(pathsave, "w+") as newsave:
                newsave.write(str(realtime))