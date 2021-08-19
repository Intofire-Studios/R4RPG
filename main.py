from extensions import cfgCreate, richPresence, cfgCheck

cfgCreate.cfgcreate('saves.ini')
cfgCheck.cfgcheck('saves.ini')

from modules import mainmenu, player

p = player.Player()

richPresence.rpc(p)
mainmenu.mainmenu(p)