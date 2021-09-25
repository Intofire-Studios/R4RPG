from extensions import cfgCreate, richPresence, cfgCheck, fileAssociation

cfgCreate.cfgcreate(fileAssociation.saves)
cfgCheck.cfgcheck(fileAssociation.saves)

from modules import mainmenu, player

p = player.Player()

richPresence.rpc(p)
mainmenu.mainmenu(p)