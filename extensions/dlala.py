from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath

def dlala(p):
    saveProcess(p, saves, lastsavepath)
    consoleClear()
    while True:
        consoleClear()
        print("---")
        print("You have entered the secret menu of the game!")
        print("---")
        print("Choose what to do!")
        print("---")
        print("1. Edit saves file")
        print("2. Exit DLALA menu")
        n = input("Number: ")
        if n == "1":
            savesedit(p)
        if n == "2":
            break        
        
def savesedit(p):
    saveProcess(p, saves, lastsavepath)
    consoleClear()
    while True:
        consoleClear()
        print("---")
        print("Choose what to edit!")
        print("---")
        print("1. Edit name")
        print("2. Edit HP")
        print("More coming soon...")
        print("3. Exit")
        n = input("Number: ")
        if n == "1":
            editname(p)
        if n == "2":
            editcls(p)
        if n == "3":
            break
        
def editname(p):
    consoleClear()
    print("---")
    print("Write your new name!")
    print("---")
    n = input("Name: ")
    p.name = n
    saveProcess(p, saves, lastsavepath)

def editcls(p):
    consoleClear()
    print("---")
    print("Set your HP!")
    print("---")
    n = input("Amount: ")
    p.hp = n
    saveProcess(p, saves, lastsavepath)