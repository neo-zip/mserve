
from rich.console import Console
import os
from time import gmtime, strftime
import json
from distutils.dir_util import copy_tree
import requests


mount = Console()
CD_CURRENT = os.getcwd()
CD_FILE = os.path.dirname(os.path.realpath(__file__))




def setInfo(title: str, description: str, symbol:str = '➜', crlf: bool = False):
    mount.print( f'[green]  {symbol} [/] [bold]{title}: [/][cyan]{description}[/]' )
    if crlf:
        print()


def getInfo(text: str):
    info = mount.input(f'[green]  ➜ [/] [bold]{text}: [/]' )
    return info



def download(url:str, path:str, name:str):
    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, name)
    r = requests.get(url, stream=True)

    if r.ok:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        setInfo('Success',f'downloaded as [green]{name}[/]','✔')
    else:
        setInfo('Failed',f'[red]download status code {r.status_code}[/]','[red]✖[/]')



def backupWorlds(path:str):
    if not os.path.exists(path):
        raise Exception('path not found')
    if not os.path.exists(path + '/.backups'):
        os.makedirs(path + '/.backups')

    bakName = strftime("%Y-%m-%d@%H.%M.%S", gmtime())

    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file == 'level.dat':
                try:
                    copy_tree(
                    subdir,
                    path + '/.backups/' + bakName + '/' + os.path.basename(os.path.normpath(subdir))
                    )
                except:pass

    setInfo('Backed',f'Backed all worlds up from [bold]{path}[/] as [bold]{bakName}[/]')



def storageAdd(path:str,obj):
    if not os.path.exists(path):
        os.makedirs(path)
 
    with open(path+'\mserve.json', 'w') as f:
        f.write(json.dumps(obj, indent=4))

def storageSet(path:str,key,value):
    if not os.path.exists(path):
        raise Exception('path not found')
    else: 
        print(key,value)

def storageGet(path:str,key:str = ''): 
    if not os.path.exists(path):
        raise Exception('path not found')
    if key == '':
        with open(path+'\mserve.json', 'r') as f:
            return json.load(f)
    else: 
        with open(path+'\mserve.json', 'r') as f:
            return json.load(f)[key]

 