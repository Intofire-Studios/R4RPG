from pypresence import Presence, exceptions
from random import randint

client_id = "876419793320837161"
RPC = Presence(client_id=client_id)

def rpc(p):
    try:
        RPC.connect()
        RPC.update(large_image="mainmenu", large_text="At main menu", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except AssertionError:
        pass
    except exceptions.InvalidPipe:
        pass

def rpcupdate(p):
    try:
        RPC.update(large_image="mainmenu", large_text="In the main menu", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except AssertionError:
        pass
    except exceptions.InvalidPipe:
        pass

def rpcfightupdate(p):
    try:
        RPC.update(large_image="menu_fight", large_text="Fighting the enemy", details="Fighting the enemy", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except AssertionError:
        pass
    except exceptions.InvalidPipe:
        pass

def rpclose(p):
    try:
        RPC.update(large_image="gameover", large_text="Game over", details="YOU'VE LOST!", state="HP: 0/{}".format(p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except AssertionError:
        pass
    except exceptions.InvalidPipe:
        pass

def rpcshopupdate(p):
    try:
        RPC.update(large_image="menu_shop", large_text="In the shop", details="Looking at what to buy in the shop...", state="Money: {}".format(p.money), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except AssertionError:
        pass
    except exceptions.InvalidPipe:
        pass

def rpcupgradeupdate(p):
    try:
        RPC.update(large_image="menu_upgrade", large_text="In Upgrade menu", details="Looking at what can be upgraded...", state="Skill points: {}".format(p.sp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except AssertionError:
        pass
    except exceptions.InvalidPipe:
        pass

def rpcstatsupdate(p):
    try:
        smth = randint(1,2)
        if smth == 1:
            RPC.update(large_image="menu_stats", large_text="Checking stats", details="Checking stats...", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        if smth == 2:
            RPC.update(large_image="menu_stats", large_text="Checking stats", details="Checking stats...", state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except AssertionError:
        pass
    except exceptions.InvalidPipe:
        pass        