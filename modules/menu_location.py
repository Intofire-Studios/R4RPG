from extensions.saveProcess import saveProcess
from extensions.richPresence import rpclocationupdate
from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath
from extensions.langSelect import lang

def menu_location(p):
    while True:
        consoleClear()
        rpclocationupdate(p)
        print("---")
        print(lang['chooselocation'] + "!")
        print("---")
        print("1. " + lang['spawn'])
        if p.sandspass == 1:
            print("2. " + lang['sands'])
        else:
            print("<" + lang['closed'] + ">")
        if p.snowkingdompass == 1:
            print("3. " + lang['snowkingdom'])
        else:
            print("<" + lang['closed'] + ">")
        n = input(lang['number'] + ": ")
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
