import urllib.request
import os
import zipfile
import shutil
import time

os.system("cls||clear")
urllib.request.urlretrieve("https://github.com/Intofire-Studios/R4RPG/archive/refs/heads/master.zip", "update.zip")
try:
    os.mkdir('updater/download')
except FileExistsError:
    pass
os.replace('update.zip', 'updater/download/update.zip')
with zipfile.ZipFile('updater/download/update.zip', 'r') as zip_ref:
    zip_ref.extractall('updater/download/')
os.remove('updater/download/update.zip')
for g in os.listdir('updater/download/R4RPG-master'):
    os.replace(f'updater/download/R4RPG-master/{g}', f'updater/download/{g}')
shutil.rmtree('updater/download/R4RPG-master')
shutil.rmtree('updater/download/updater')
shutil.rmtree('extensions')
shutil.rmtree('modules')
os.remove('.gitignore')
os.remove('main.py')
os.remove('README.md')
os.remove('requirements.txt')
os.remove('start.bat')
os.remove('start.sh')
for g in os.listdir('updater/download'):
    os.replace(f'updater/download/{g}', g)

for percent in range(100):
    s = f"[{(percent // 10) * '■'}"
    s += f"{(10 - (percent // 10)) * '○'}] "
    s += f"{percent}"
    print('Downloading the update... ', s, end="\r")
    time.sleep(0.1)

os.system("cls||clear")
print('Update completed. Launching the game...')
time.sleep(3)
os.system('python main.py')