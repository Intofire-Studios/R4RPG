from sys import platform
from os import system

def consoleClear():
    if platform in ["linux", "linux2"]:
        system("reset")
    elif platform == "win32":
        system("cls")