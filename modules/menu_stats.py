from extensions.richPresence import rpcstatsupdate
from extensions.cmdClear import consoleClear
from extensions.langSelect import lang

def menu_stats(p):
    rpcstatsupdate(p)
    consoleClear()
    print("---")
    print(lang['stats'] + "!")
    print("---")
    print(lang['name'] + f": {p.name}")
    print(lang['cls'] + f": {p.cls}")
    print(lang['lvl'] + f": {p.level}")
    print(lang['xp'] + f": {p.xp}/{p.max_xp}")
    print(lang['hp'] + f": {p.hp}/{p.max_hp}")
    print(lang['power'] + f": {p.pw}")
    print(lang['healing'] + f": {p.heal_hp}")
    print(lang['pwrboost'] + f": {p.plus_pw}")
    print("---")
    print(lang['pwpotions'] + f": {p.pwpotion}")
    print(lang['healpotions'] + f": {p.hppotion}")
    print("---")
    print(lang['travelpasses'] + ":")
    print("- " + lang['spawnpass'])
    if p.sandspass == 1:
        print("- " + lang['sandspass'])
    if p.snowkingdompass == 1:
        print("- " + lang['snowkingdompass'])
    print("---")
    input(lang['ntrtocontinue'] + ".")
    consoleClear()