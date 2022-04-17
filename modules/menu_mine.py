from random import choice
from time import sleep
from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcmineupdate
from extensions.fileAssociation import saves, lastsavepath
from modules.mine_modules import blocks, blockcheck, blocktoinventory

def menu_mine(p):
    while p.pickaxe > 0:
        block = choice(blocks.blocks)
        blockstrength = blockcheck.blockcheck(block)
        rpcmineupdate(p)
        saveProcess(p, saves, lastsavepath)
        consoleClear()
        print("---")
        print(f"{p.name}'s pickaxe: {p.pickaxe}/{p.max_pickaxe}.")
        print(f"Block: {block}. Block strength: {blockstrength}")
        print("---")
        print("1. Mine the block")
        print("2. Exit to main menu")
        n = input("Number: ")
        if n == "1":
            if p.pickaxe >= blockstrength:
                p.pickaxe -= blockstrength
                blocktoinventory.blocktoinventory(p, block)
                saveProcess(p, saves, lastsavepath)
            else:
                consoleClear()
                print("Your pickaxe is not good enough to mine this block... After trying to get the block, it broke down.")
                p.pickaxe = 0
                sleep(3)
                break
        if n == "2":
            break
