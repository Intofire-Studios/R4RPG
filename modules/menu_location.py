from extensions.cfgSave import cfgsave
from extensions.richPresence import rpcupdate
from extensions.cmdClear import consoleClear

def menu_location(p):
    while True:
        consoleClear()
        rpcupdate(p)
        print("---")
        print("Choose next location!")
        print("---")
        print("1. Spawn")
        if p.sandspass == 1:
            print("2. Sands")
        else:
            print("<CLOSED>")
        n = input("Number: ")
        if n == "1":
            p.location = "spawn"
            cfgsave(p, 'saves.ini')
            rpcupdate(p)
            return False
        if n == "2" and p.sandspass == 1:
            p.location = "sands"
            cfgsave(p, 'saves.ini')
            rpcupdate(p)
            return False
