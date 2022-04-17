from extensions import richPresence, fileAssociation, saveCreate, saveCheck, savePort, saveCheatCheck

saveCheatCheck.saveCheatCheck(fileAssociation.lastsavepath, fileAssociation.saves)
savePort.savePort(fileAssociation.lastsavepath, fileAssociation.saves)
saveCreate.saveCreate(fileAssociation.lastsavepath, fileAssociation.saves)
saveCheck.saveCheck(fileAssociation.lastsavepath, fileAssociation.saves)

from modules import mainmenu, player

p = player.Player()

richPresence.rpc(p)
mainmenu.mainmenu(p)