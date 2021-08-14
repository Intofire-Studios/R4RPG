import os
from extensions.cfgCreate import cfgcreate as cfgcreate
from extensions.cmdClear import consoleClear as consoleClear

if not os.path.exists('saves.ini'):
    consoleClear()
    cfgcreate('saves.ini')

from modules import mainmenu, player

p = player.Player()

consoleClear()
mainmenu.mainmenu(p)