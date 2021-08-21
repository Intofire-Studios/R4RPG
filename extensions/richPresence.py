from pypresence import Presence, exceptions
from random import randint

client_id = "876419793320837161"
RPC = Presence(client_id=client_id)

def rpc(p):
    try:
        RPC.connect()
        if p.location == "spawn":
            RPC.update(large_image="mainmenu", large_text="At main menu", small_image="spawn", small_text="Location: Spawn", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            RPC.update(large_image="mainmenu", large_text="At main menu", small_image="sands", small_text="Location: Sands", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            RPC.update(large_image="mainmenu", large_text="At main menu", small_image="snowkingdom", small_text="Location: Snow kingdom", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcupdate(p):
    try:
        if p.location == "spawn":
            RPC.update(large_image="mainmenu", large_text="At main menu", small_image="spawn", small_text="Location: Spawn", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            RPC.update(large_image="mainmenu", large_text="At main menu", small_image="sands", small_text="Location: Sands", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            RPC.update(large_image="mainmenu", large_text="At main menu", small_image="snowkingdom", small_text="Location: Snow kingdom", details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcfightupdate(p):
    try:
        if p.location == "spawn":
            RPC.update(large_image="menu_fight", large_text="Fighting the enemy", small_image="spawn", small_text="Location: Spawn", details="Fighting the enemy", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            RPC.update(large_image="menu_fight", large_text="Fighting the enemy", small_image="sands", small_text="Location: Sands", details="Fighting the enemy", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            RPC.update(large_image="menu_fight", large_text="Fighting the enemy", small_image="snowkingdom", small_text="Location: Snow kingdom", details="Fighting the enemy", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpclose(p):
    try:
        if p.location == "spawn":
            RPC.update(large_image="gameover", large_text="Game over", small_image="spawn", small_text="Location: Spawn", details="YOU'VE LOST!", state="HP: 0/{}".format(p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            RPC.update(large_image="gameover", large_text="Game over", small_image="sands", small_text="Location: Sands", details="YOU'VE LOST!", state="HP: 0/{}".format(p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            RPC.update(large_image="gameover", large_text="Game over", small_image="snowkingdom", small_text="Location: Snow kingdom", details="YOU'VE LOST!", state="HP: 0/{}".format(p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcshopupdate(p):
    try:
        if p.location == "spawn":
            RPC.update(large_image="menu_shop", large_text="In the shop", small_image="spawn", small_text="Location: Spawn", details="Looking at what to buy in the shop...", state="Money: {}".format(p.money), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            RPC.update(large_image="menu_shop", large_text="In the shop", small_image="sands", small_text="Location: Sands", details="Looking at what to buy in the shop...", state="Money: {}".format(p.money), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            RPC.update(large_image="menu_shop", large_text="In the shop", small_image="snowkingdom", small_text="Location: Snow kingdom", details="Looking at what to buy in the shop...", state="Money: {}".format(p.money), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcupgradeupdate(p):
    try:
        if p.location == "spawn":
            RPC.update(large_image="menu_upgrade", large_text="In Upgrade menu", small_image="spawn", small_text="Location: Spawn", details="Looking at what can be upgraded...", state="Skill points: {}".format(p.sp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            RPC.update(large_image="menu_upgrade", large_text="In Upgrade menu", small_image="sands", small_text="Location: Sands", details="Looking at what can be upgraded...", state="Skill points: {}".format(p.sp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            RPC.update(large_image="menu_upgrade", large_text="In Upgrade menu", small_image="snowkingdom", small_text="Location: Snow kingdom", details="Looking at what can be upgraded...", state="Skill points: {}".format(p.sp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcstatsupdate(p):
    try:
        smth = randint(1,2)
        if p.location == "spawn":
            if smth == 1:
                RPC.update(large_image="menu_stats", large_text="Checking stats", small_image="spawn", small_text="Location: Spawn", details="Checking stats...", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
            if smth == 2:
                RPC.update(large_image="menu_stats", large_text="Checking stats", small_image="spawn", small_text="Location: Spawn", details="Checking stats...", state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            if smth == 1:
                RPC.update(large_image="menu_stats", large_text="Checking stats", small_image="sands", small_text="Location: Sands", details="Checking stats...", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
            if smth == 2:
                RPC.update(large_image="menu_stats", large_text="Checking stats", small_image="sands", small_text="Location: Sands", details="Checking stats...", state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            if smth == 1:
                RPC.update(large_image="menu_stats", large_text="Checking stats", small_image="snowkingdom", small_text="Location: Snow kingdom", details="Checking stats...", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
            if smth == 2:
                RPC.update(large_image="menu_stats", large_text="Checking stats", small_image="snowkingdom", small_text="Location: Snow kingdom", details="Checking stats...", state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpclocationupdate(p):
    try:
        if p.location == "spawn":
            RPC.update(large_image="menu_location", large_text="Changing the location", small_image="spawn", small_text="Location: Spawn", details="Changing the location...", state="Current location: {}".format(p.location), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "sands":
            RPC.update(large_image="menu_location", large_text="Changing the location", small_image="sands", small_text="Location: Sands", details="Changing the location...", state="Current location: {}".format(p.location), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        elif p.location == "snow kingdom":
            RPC.update(large_image="menu_location", large_text="Changing the location", small_image="snowkingdom", small_text="Location: Snow kingdom", details="Changing the location...", state="Current location: {}".format(p.location), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass