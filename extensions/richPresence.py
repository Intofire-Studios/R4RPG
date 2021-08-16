from pypresence import Presence
from random import randint

client_id = "876419793320837161"
RPC = Presence(client_id=client_id)

def rpc(p):
    if p.discordstatus == "yes":
        RPC.connect()

        RPC.update(details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpcupdate(p):
    if p.discordstatus == "yes":
        RPC.update(details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpcfightupdate(p):
    if p.discordstatus == "yes":
        RPC.update(details="Fighting the enemy", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpclose(p):
    if p.discordstatus == "yes":
        RPC.update(details="YOU'VE LOST!", state="HP: 0/{}".format(p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    
def rpcshopupdate(p):
    if p.discordstatus == "yes":
        RPC.update(details="Looking at what to buy in the shop...", state="Money: {}".format(p.money), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpcupgradeupdate(p):
    if p.discordstatus == "yes":
        RPC.update(details="Looking at what can be upgraded...", state="Skill points: {}".format(p.sp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpcstatsupdate(p):
    if p.discordstatus == "yes":
        smth = randint(1,2)
        if smth == 1:
            RPC.update(details="Checking stats...", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        if smth == 2:
            RPC.update(details="Checking stats...", state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])