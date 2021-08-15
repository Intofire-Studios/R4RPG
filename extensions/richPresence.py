from pypresence import Presence

client_id = "876419793320837161"
RPC = Presence(client_id=client_id)

def rpc(p):
    RPC.connect()

    RPC.update(details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpcupdate(p):
    RPC.update(details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpcfightupdate(p):
    RPC.update(details="Fighting the enemy", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])

def rpclose(p):
    RPC.update(details="YOU'VE LOST!", state="HP: 0/{}".format(p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])