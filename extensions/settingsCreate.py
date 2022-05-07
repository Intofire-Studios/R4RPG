import sqlite3
from sqlite3 import Error
import os
from extensions.cmdClear import consoleClear
import subprocess
from sys import platform

def create_connection(settingspath):
    connection = None
    try:
        connection = sqlite3.connect(settingspath)
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
def settingsCreate(settingspath):
    
    consoleClear()

    if os.path.exists(settingspath):
        return
    newsave = open(settingspath, "w+")
    newsave.close()
    if platform == "win32":
        subprocess.call(['attrib', '+h', settingspath])
    connection = create_connection(settingspath)

    create_settings_table = """
        CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY,
        lang TEXT NOT NULL
        );
        """

    execute_query(connection, create_settings_table)

    d = 0
    while d != 1:
        print("Choose language!")
        print("1. English")
        print("2. Русский (Russian)")
        print("3. Українська (Ukranian)")
        n = input("Number: ")
        if n == "1":
            lang = 'en'
            d = 1
        elif n == "2":
            lang = 'ru'
            d = 1
        elif n == "3":
            lang = 'ua'
            d = 1


    create_settings = """
        INSERT INTO
            settings (id, lang)
        VALUES
            (?, ?)
        """

    data = (1, lang)

    connection.execute(create_settings, data)
    connection.commit()
    connection.close()