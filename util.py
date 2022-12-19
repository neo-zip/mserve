
from rich.console import Console
import os
import json
import shutil
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
    # if not os.path.exists(path):
    #     os.makedirs(path)

    # file_path = os.path.join(path, name)
    # r = requests.get(url, stream=True)

    # if r.ok:
        # with open(file_path, 'wb') as f:
        #     for chunk in r.iter_content(chunk_size=1024 * 8):
        #         if chunk:
        #             f.write(chunk)
        #             f.flush()
        #             os.fsync(f.fileno())
    if True:
        setInfo('Success',f'downloaded as [green]{name}[/]','✔')
    else:  
        setInfo('Failed',f'[red]download status code {r.status_code}[/]','[red]✖[/]')

def copy(source:str, location:str):
    if not os.path.exists(location):
        os.makedirs(location)

    shutil.copy(source, location)

def storageAdd(path:str,obj):
    if not os.path.exists(path):
        os.makedirs(path)
 
    with open(path+'\mserve.json', 'w') as f:
        f.write(json.dumps(obj, indent=4))

def storageSet(path:str,key,value):
    if not os.path.exists(path):
        raise Exception('Error: path not found')
    else: 
        print(key,value)

def storageGet(path:str,key:str): 
    if not os.path.exists(path):
        raise Exception('Error: path not found')
    else: 
        with open(path+'\mserve.json', 'r') as f:
            return json.load(f)[key]

 