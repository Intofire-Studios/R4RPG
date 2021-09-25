from pypresence import Presence, exceptions
from random import randint

client_id = "876419793320837161"
RPC = Presence(client_id=client_id)

def rpc(p):
    try:
        RPC.connect()
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcupdate(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="mainmenu", large_text="At main menu", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="HP: {}/{}".format(p.hp, p.max_hp), state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcfightupdate(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="menu_fight", large_text="Fighting the enemy", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Fighting the enemy", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpclose(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="gameover", large_text="Game over", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="YOU'VE LOST!", state="HP: 0/{}".format(p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcshopupdate(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="menu_shop", large_text="In the shop", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Looking at what to buy in the shop...", state="Money: {}".format(p.money), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcupgradeupdate(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="menu_upgrade", large_text="In Upgrade menu", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Looking at what can be upgraded...", state="Skill points: {}".format(p.sp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcstatsupdate(p):
    try:
        smth = randint(1,2)
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        if smth == 1:
            RPC.update(large_image="menu_stats", large_text="Checking stats", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Checking stats...", state="HP: {}/{}".format(p.hp, p.max_hp), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
        if smth == 2:
            RPC.update(large_image="menu_stats", large_text="Checking stats", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Checking stats...", state="Power: {}".format(p.pw), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpclocationupdate(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="menu_location", large_text="Changing the location", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Changing the location...", state="Current location: {}".format(p.location), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcmineupdate(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="menu_mine", large_text="Digging something in the mine...", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Digging something in the mine...", state="Pickaxe: {}/{}".format(p.pickaxe, p.max_pickaxe), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass

def rpcinventoryupdate(p):
    try:
        if p.location == "spawn":
            location = "spawn"
        elif p.location == "sands":
            location = "sands"
        elif p.location == "snow kingdom":
            location = "snowkingdom"
        RPC.update(large_image="menu_inventory", large_text="Checking inventory...", small_image=location, small_text="Location: {}".format(p.location).capitalize(), details="Checking inventory...", state="Pickaxe: {}/{}".format(p.pickaxe, p.max_pickaxe), buttons=[{"label": "Website", "url": "https://github.com/Rarmash/R4RPG"}])
    except (AssertionError, exceptions.InvalidPipe):
        pass