from extensions import richPresence, fileAssociation
from extensions import saveCreate, saveCheck

saveCreate.saveCreate(fileAssociation.saves)
saveCheck.saveCheck(fileAssociation.saves)

from modules import mainmenu, player

p = player.Player()

richPresence.rpc(p)
mainmenu.mainmenu(p)