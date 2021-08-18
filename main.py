from extensions import cfgCreate, richPresence

cfgCreate.cfgcreate('saves.ini')

from modules import mainmenu, player

p = player.Player()

richPresence.rpc(p)
mainmenu.mainmenu(p)