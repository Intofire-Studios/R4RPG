from random import choice
from time import time
from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcupgradeupdate
from extensions.fileAssociation import saves
from modules.mine_modules import blocks, blockcheck, blocktoinventory

def menu_mine(p):
    rpcupgradeupdate(p)
    block = choice(blocks.blocks)
    blockstrength = blockcheck.blockcheck(block)
    while p.pickaxe > 0:
        cfgsave(p, saves)
        consoleClear()
        print("---")
        print("{}'s pickaxe: {}/{}.".format(p.name, p.pickaxe,p.max_pickaxe))
        print("Block: {}. Block strength: {}".format(block, blockstrength))
        print("---")
        print("1. Mine the block")
        print("2. Exit to main menu")
        n = input("Number: ")
        if n == "1":
            if p.pickaxe >= blockstrength:
                p.pickaxe -= blockstrength
                blocktoinventory.blocktoinventory(p, block)
                cfgsave(p, saves)
            else:
                print("Your pickaxe is not good enough to mine this block...")
                time.sleep(3)
                break
        if n == "2":
            break
