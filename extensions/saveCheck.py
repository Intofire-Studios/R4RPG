import sqlite3
from sqlite3 import OperationalError
from extensions.saveCreate import execute_query
import os
        
def saveCheck(pathsave, path):
    sqlite_connection = sqlite3.connect(path)
    cursor = sqlite_connection.cursor()
    
    try:
        cursor.execute("SELECT id FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN id INTEGER PRIMARY KEY "0"
            """
        execute_query(sqlite_connection, create_save_table)

    try:
        cursor.execute("SELECT name FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN name TEXT NOT NULL "Player"
            """
        execute_query(sqlite_connection, create_save_table)

    try:
        cursor.execute("SELECT cls FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN cls TEXT NOT NULL "Heavy"
            """
        execute_query(sqlite_connection, create_save_table)

    try:
        cursor.execute("SELECT hp FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN hp INTEGER "25"
            """
        execute_query(sqlite_connection, create_save_table)

    try:
        cursor.execute("SELECT max_hp FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN max_hp INTEGER "25"
            """
        execute_query(sqlite_connection, create_save_table)

    try:
        cursor.execute("SELECT heal_hp FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN heal_hp INTEGER "5"
            """
        execute_query(sqlite_connection, create_save_table)
        
    try:
        cursor.execute("SELECT pw FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN pw INTEGER "2"
            """
        execute_query(sqlite_connection, create_save_table)

    try:
        cursor.execute("SELECT level FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN level INTEGER "1"
            """
        execute_query(sqlite_connection, create_save_table)

    try:
        cursor.execute("SELECT sp FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN sp INTEGER "0"
            """
        execute_query(sqlite_connection, create_save_table)
        
    try:
        cursor.execute("SELECT money FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN money INTEGER "0"
            """
        execute_query(sqlite_connection, create_save_table)
        
    try:
        cursor.execute("SELECT xp FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN xp INTEGER "0"
            """
        execute_query(sqlite_connection, create_save_table)
        
    try:
        cursor.execute("SELECT plus_pw FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN plus_pw INTEGER "1"
            """
        execute_query(sqlite_connection, create_save_table)
            
    try:
        cursor.execute("SELECT max_xp FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN max_xp INTEGER "5"
            """
        execute_query(sqlite_connection, create_save_table)
                
    try:
        cursor.execute("SELECT pwpotion FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN pwpotion INTEGER "0"
            """
        execute_query(sqlite_connection, create_save_table)
                    
    try:
        cursor.execute("SELECT hppotion FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN hppotion INTEGER "10"
            """
        execute_query(sqlite_connection, create_save_table)
                            
    try:
        cursor.execute("SELECT location FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN location TEXT "spawn"
            """
        execute_query(sqlite_connection, create_save_table)
        
    try:
        cursor.execute("SELECT sandspass FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN sandspass INTEGER "0"
            """
        execute_query(sqlite_connection, create_save_table)
                
    try:
        cursor.execute("SELECT snowkingdompass FROM save;")
    except OperationalError:
        create_save_table = """
            ALTER TABLE save ADD COLUMN snowkingdompass INTEGER "0"
            """
        execute_query(sqlite_connection, create_save_table)
        
    try:
        cursor.execute("SELECT id FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN id INTEGER PRIMARY KEY "1"
            """
        execute_query(sqlite_connection, create_inventory_table)
                
    try:
        cursor.execute("SELECT pickaxe FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN pickaxe INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                        
    try:
        cursor.execute("SELECT max_pickaxe FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN max_pickaxe INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                
    try:
        cursor.execute("SELECT stone FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN stone INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                
    try:
        cursor.execute("SELECT copper FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN copper INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                
    try:
        cursor.execute("SELECT tin FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN tin INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                        
    try:
        cursor.execute("SELECT iron FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN iron INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                            
    try:
        cursor.execute("SELECT aluminum FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN aluminum INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                                    
    try:
        cursor.execute("SELECT silver FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN silver INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                                            
    try:
        cursor.execute("SELECT topaz FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN topaz INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                                                    
    try:
        cursor.execute("SELECT gold FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN gold INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
        
    try:
        cursor.execute("SELECT crystal FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN crystal INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                
    try:
        cursor.execute("SELECT diamond FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN diamond INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                        
    try:
        cursor.execute("SELECT emerald FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN emerald INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
                                
    try:
        cursor.execute("SELECT ruby FROM inventory;")
    except OperationalError:
        create_inventory_table = """
            ALTER TABLE save ADD COLUMN ruby INTEGER "0"
            """
        execute_query(sqlite_connection, create_inventory_table)
        
    sqlite_connection.commit()
    sqlite_connection.close()
    
    realtime = os.path.getmtime(path)
    if not os.path.exists(pathsave):
        with open(pathsave, "w+") as newsave:
            newsave.write(str(realtime))
    else:
        os.remove(pathsave)
        with open(pathsave, "w+") as newsave:
            newsave.write(str(realtime))