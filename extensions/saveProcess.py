import sqlite3
import os

def saveProcess(p, path, pathsave):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute("""
                   DELETE from save where id = 1
                   """)
    cursor.execute("""
                   DELETE from inventory where id = 1
                   """)
    cursor.close()

    create_save = """
    INSERT INTO
        save (id, name, cls, hp, max_hp, heal_hp, pw, level, sp, money, xp, plus_pw, max_xp, pwpotion, hppotion, location, sandspass, snowkingdompass)
    VALUES
        (1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    data = (p.name, p.cls, p.hp, p.max_hp, p.heal_hp, p.pw, p.level, p.sp, p.money, p.xp, p.plus_pw, p.max_xp, p.pwpotion, p.hppotion, p.location, p.sandspass, p.snowkingdompass)

    create_inventory = """
        INSERT INTO
        inventory (id, pickaxe, max_pickaxe, stone, copper, tin, iron, aluminum, silver, topaz, gold, crystal, diamond, emerald, ruby, sword, max_sword, damage, armor, max_armor)
    VALUES
        (1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    data1 = (p.pickaxe, p.max_pickaxe, p.stone, p.copper, p.tin, p.iron, p.aluminum, p.silver, p.topaz, p.gold, p.crystal, p.diamond, p.emerald, p.ruby, p.sword, p.max_sword, p.damage, p.armor, p.max_armor)
    connection.execute(create_save, data)
    connection.execute(create_inventory, data1)
    connection.commit()
    connection.close()

    realtime = os.path.getmtime(path)
    if os.path.exists(pathsave):
        os.remove(pathsave)
    with open(pathsave, "w+") as newsave:
        newsave.write(str(realtime))