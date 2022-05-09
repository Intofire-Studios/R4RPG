from extensions.richPresence import rpcinventoryupdate
from extensions.cmdClear import consoleClear
from extensions.langSelect import lang

def menu_inventory(p):
    rpcinventoryupdate(p)
    consoleClear()
    print("---")
    print(f"{p.name}" + lang['inventory'] + "!")
    print("---")
    print(lang['pickaxe'] + f": {p.pickaxe}/{p.max_pickaxe}")
    print(lang['sword'] + f": {p.damage} ({p.sword}/{p.max_sword})")
    print(lang['armor'] + f": {p.armor}/{p.max_armor}")
    if p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0:
        print("---")
    if p.stone != 0:
        print(lang['stone'] + f": {p.stone}")
    if p.copper != 0:
        print(lang['copper'] + f": {p.copper}")
    if p.tin != 0:
        print(lang['tin'] + f": {p.tin}")
    if p.iron != 0:
        print(lang['iron'] + f": {p.iron}")
    if p.aluminum != 0:
        print(lang['aluminum'] + f": {p.aluminum}")
    if p.silver != 0:
        print(lang['silver'] + f": {p.silver}")
    if p.topaz != 0:
        print(lang['topaz'] + f": {p.topaz}")
    if p.gold != 0:
        print(lang['gold'] + f": {p.gold}")
    if p.crystal != 0:
        print(lang['crystal'] + f": {p.crystal}")
    if p.diamond != 0:
        print(lang['diamond'] + f": {p.diamond}")
    if p.ruby != 0:
        print(lang['ruby'] + f": {p.ruby}")
    if p.emerald != 0:
        print(lang['emerald'] + f": {p.emerald}")
    print("---")
    input(lang['ntrtocontinue'] + ".")
    consoleClear()