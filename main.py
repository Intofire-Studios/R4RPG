import os
from extensions.cfgCreate import cfgcreate as cfgcreate
from extensions.cmdClear import consoleClear as consoleClear

if not os.path.exists('saves.ini'):
    consoleClear()
    cfgcreate('saves.ini')

from modules import menu_upgrade, mainmenu, player

p = player.Player()

menu_upgrade.menu_upgrade(p)
consoleClear()
mainmenu.mainmenu(p)