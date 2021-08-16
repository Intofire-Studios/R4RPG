import os
from extensions.cfgCreate import cfgcreate
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpc

if not os.path.exists('saves.ini'):
    consoleClear()
    cfgcreate('saves.ini')

from modules import mainmenu, player

p = player.Player()

rpc(p)
consoleClear()
mainmenu.mainmenu(p)