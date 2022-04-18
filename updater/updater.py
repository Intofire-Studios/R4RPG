import urllib.request
import os
import zipfile
import shutil

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
    os.replace('updater/download/R4RPG-master/'+ g, 'updater/download/' + g)
shutil.rmtree('updater/download/R4RPG-master')
shutil.rmtree('extensions')
shutil.rmtree('modules')
os.remove('.gitignore')
os.remove('main.py')
os.remove('README.md')
os.remove('requirements.txt')
os.remove('start.bat')
os.remove('start.sh')
for g in os.listdir('updater/download'):
    os.replace('updater/download/'+ g, g)