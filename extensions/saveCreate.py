import sqlite3
from sqlite3 import Error
import os

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
def saveCreate(path):
    if os.path.exists(path):
        return
    newsave = open("saves.sqlite", "w+")
    newsave.close()
    connection = create_connection(path)

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

    execute_query(connection, create_save_table)
    execute_query(connection, create_inventory_table)   

    name = input("Enter your name: ")
    d = 0
    while d != 1:
        cls = input("Enter desired character class (Heavy, Medic or Warrior): ")
        if cls.lower() == "heavy":
            cls = "Heavy"
            hp = 25
            max_hp = 25
            heal_hp = 5
            pw = 2
            d = 1
        elif cls.lower() == "medic":
            cls = "Medic"
            hp = 10
            max_hp = 10
            heal_hp = 15
            pw = 2
            d = 1
        elif cls.lower() == "warrior":
            cls = "Warrior"
            hp = 10
            max_hp = 10
            heal_hp = 5
            pw = 6
            d = 1
        else:
            d = 0   

    create_save = """
        INSERT INTO
            save (id, name, cls, hp, max_hp, heal_hp, pw, level, sp, money, xp, plus_pw, max_xp, pwpotion, hppotion, location, sandspass, snowkingdompass)
        VALUES
            (1, ?, ?, ?, ?, ?, ?, 1, 0, 0, 0, 1, 5, 0, 10, 'spawn', 0, 0)
        """

    data = (name, cls, hp, max_hp, heal_hp, pw)

    create_inventory = """
            INSERT INTO
            inventory (id, pickaxe, max_pickaxe, stone, copper, tin, iron, aluminum, silver, topaz, gold, crystal, diamond, emerald, ruby)
        VALUES
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        """

    connection.execute(create_save, data)
    execute_query(connection, create_inventory)
    connection.commit()
    connection.close()