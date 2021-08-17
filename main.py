import os
from extensions import cfgCreate, cmdClear, richPresence

if not os.path.exists('saves.ini'):
    cmdClear.consoleClear()
    cfgCreate.cfgcreate('saves.ini')

from modules import mainmenu, player

p = player.Player()

richPresence.rpc(p)
mainmenu.mainmenu(p)