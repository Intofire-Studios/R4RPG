from extensions.saveProcess import saveProcess
from extensions.richPresence import rpclocationupdate
from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath

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
            saveProcess(p, saves, lastsavepath)
            rpclocationupdate(p)
            return False
        if n == "2" and p.sandspass == 1:
            p.location = "sands"
            saveProcess(p, saves, lastsavepath)
            rpclocationupdate(p)
            return False
        if n == "3" and p.snowkingdompass == 1:
            p.location = "snow kingdom"
            saveProcess(p, saves, lastsavepath)
            rpclocationupdate(p)
            return False
