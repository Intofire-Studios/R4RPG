import requests
def versionChecher():
    try:
        info = requests.get('https://raw.githubusercontent.com/Intofire-Studios/R4RPG/master/extensions/version.txt')
        with open('extensions/version.txt', 'r') as f:
            curver = f.read()[:-1]
        return 1 if str(info.content)[2:-3] == curver else 0
    except:
        return 0