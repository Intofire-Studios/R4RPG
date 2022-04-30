import sqlite3

connection = sqlite3.connect('saves.sqlite')
cursor = connection.cursor()
class Player:
    cursor.execute("SELECT * FROM save;")
    name = cursor.fetchone()[1]
    cursor.execute("SELECT * FROM save;")
    cls = cursor.fetchone()[2]
    cursor.execute("SELECT * FROM save;")
    hp = cursor.fetchone()[3]
    cursor.execute("SELECT * FROM save;")
    max_hp = cursor.fetchone()[4]
    cursor.execute("SELECT * FROM save;")
    heal_hp = cursor.fetchone()[5]
    cursor.execute("SELECT * FROM save;")
    pw = cursor.fetchone()[6]
    cursor.execute("SELECT * FROM save;")
    level = cursor.fetchone()[7]
    cursor.execute("SELECT * FROM save;")
    sp = cursor.fetchone()[8]
    cursor.execute("SELECT * FROM save;")
    money = cursor.fetchone()[9]
    cursor.execute("SELECT * FROM save;")
    xp = cursor.fetchone()[10]
    cursor.execute("SELECT * FROM save;")
    plus_pw = cursor.fetchone()[11]
    cursor.execute("SELECT * FROM save;")
    max_xp = cursor.fetchone()[12]
    cursor.execute("SELECT * FROM save;")
    pwpotion = cursor.fetchone()[13]
    cursor.execute("SELECT * FROM save;")
    hppotion = cursor.fetchone()[14]
    cursor.execute("SELECT * FROM save;")
    location = cursor.fetchone()[15]
    cursor.execute("SELECT * FROM save;")
    sandspass = cursor.fetchone()[16]
    cursor.execute("SELECT * FROM save;")
    snowkingdompass = cursor.fetchone()[17]

    cursor.execute("SELECT * FROM inventory;")
    pickaxe = cursor.fetchone()[1]
    cursor.execute("SELECT * FROM inventory;")
    max_pickaxe = cursor.fetchone()[2]
    cursor.execute("SELECT * FROM inventory;")
    stone = cursor.fetchone()[3]
    cursor.execute("SELECT * FROM inventory;")
    copper = cursor.fetchone()[4]
    cursor.execute("SELECT * FROM inventory;")
    tin = cursor.fetchone()[5]
    cursor.execute("SELECT * FROM inventory;")
    iron = cursor.fetchone()[6]
    cursor.execute("SELECT * FROM inventory;")
    aluminum = cursor.fetchone()[7]
    cursor.execute("SELECT * FROM inventory;")
    silver = cursor.fetchone()[8]
    cursor.execute("SELECT * FROM inventory;")
    topaz = cursor.fetchone()[9]
    cursor.execute("SELECT * FROM inventory;")
    gold = cursor.fetchone()[10]
    cursor.execute("SELECT * FROM inventory;")
    crystal = cursor.fetchone()[11]
    cursor.execute("SELECT * FROM inventory;")
    diamond = cursor.fetchone()[12]
    cursor.execute("SELECT * FROM inventory;")
    emerald = cursor.fetchone()[13]
    cursor.execute("SELECT * FROM inventory;")
    ruby = cursor.fetchone()[14]
    cursor.execute("SELECT * FROM inventory;")
    sword = cursor.fetchone()[15]
    cursor.execute("SELECT * FROM inventory;")
    max_sword = cursor.fetchone()[16]
    cursor.execute("SELECT * FROM inventory;")
    damage = cursor.fetchone()[17]
    cursor.execute("SELECT * FROM inventory;")
    armor = cursor.fetchone()[18]
    cursor.execute("SELECT * FROM inventory;")
    max_armor = cursor.fetchone()[19]
    connection.close()