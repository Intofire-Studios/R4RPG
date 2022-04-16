import requests
def versionChecher():
    try:
        info = requests.get('https://raw.githubusercontent.com/Intofire-Studios/R4RPG/master/extensions/version.txt')
        with open('extensions/version.txt', 'r') as f:
            curver = f.read()[9:-1]
        ver = int(str(info.content)[11:-3].replace('.', ''))
        curver = int(curver.replace('.', ''))
        if ver > curver:
            return 1
        elif ver < curver:
            return 2
        else:
            return 0
    except Exception:
        return 0