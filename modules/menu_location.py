from extensions.cfgSave import cfgsave
from extensions.richPresence import rpclocationupdate
from extensions.cmdClear import consoleClear

def menu_location(p):
    while True:
        consoleClear()
        rpclocationupdate(p)
        print("---")
        print("Choose next location!")
        print("---")
        print("1. Spawn")
        if p.sandspass == 1:
            print("2. Sands")
        else:
            print("<CLOSED>")
        if p.snowkingdompass == 1:
            print("3. Snow Kingdom")
        else:
            print("<CLOSED>")
        n = input("Number: ")
        if n == "1":
            p.location = "spawn"
            cfgsave(p, 'saves.ini')
            rpclocationupdate(p)
            return False
        if n == "2" and p.sandspass == 1:
            p.location = "sands"
            cfgsave(p, 'saves.ini')
            rpclocationupdate(p)
            return False
        if n == "3" and p.snowkingdompass == 1:
            p.location = "snow kingdom"
            cfgsave(p, 'saves.ini')
            rpclocationupdate(p)
            return False
