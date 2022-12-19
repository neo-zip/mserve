#
# https://neotap.net
# MIT licence: made with <3 from neo
#


import os
import json
import sys
import requests
from rich import box
from rich.console import Console
from rich.progress import track
from rich.table import Table
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

class synLight(RegexHighlighter):
    highlights = [r'1234567890.']
c = Console(highlighter=synLight(), theme=Theme({
    'low_success': 'green',
    'error': 'red bold',
    'data': 'cyan'
}))
args = sys.argv
cd_current = os.getcwd()
cd_file = os.path.dirname(os.path.realpath(__file__))

def setInfo(title: str, description: str, *crlf: bool):
    c.print( f'[green]  ➜ [/] [bold]{title}: [/][data]{description}[/]' )
    if crlf:
        print()

def getInfo(text: str):
    info = c.input(f'[green]  ➜ [/] [bold]{text}: [/]' )
    return info

def download(url: str, folder: str):
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = url.split('/')[-1].replace(" ", "_")
    print(filename)
    file_path = os.path.join(folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            # track(range(20), description="Processing...")
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  
        print("Download failed: status code {}".format(r.status_code))

# download("https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar", folder="mydir")

def mserve_exe():
    if ( len(args) == 1 ):
        c.print('\n[magenta bold]MSERVE [/][magenta]v1.0.0[/]')
        c.print('use \'mserve help\' for help')
        c.print('site: [data]https://neotap.net/mc[/]')
    else:
        if ( args[1] == 'help' ):
            table = Table(box=box.ROUNDED)

            table.add_column('command', style='green bold')
            table.add_column('arguments')
            table.add_column('description', style='white')

            table.add_row('help', '-', 'shows this message')
            table.add_row('init', '-', 'creates a new server')
            table.add_row('start', '<server>/*', 'starts a server or lists avaliable')
            table.add_row('backup', '<server>/*', 'backs up a server\'s worlds (world_*)')
            table.add_row('util', 'kill/mysql', 'other utilities')

            c.print(table)


        elif ( args[1] == 'init' ):

            init_data = [{}]

            c.print('[magenta bold]INITILIZATION[/]\n[data]options to setup a new sever\nand dont worry, you can change most options later. \n[bold green]Press enter to skip (sets default)[/]')


            init_data.append(getInfo('Path (skip to set current dir/...)'))
            if init_data[0] == '':
                init_data[0] = '.'
            # elif not os.path.exists(init_data[0]):
            #     os.makedirs(init_data[0])
            
            
            init_data.append(getInfo('Type (Normal/Proxy)'))
            if init_data[1].lower() != 'proxy':
                getInfo('Provider (Paper/Sigot/Vanilla)')
                if init_data[1].lower() != 'vanilla' or init_data[1].lower() != 'spigot':
                    init_data[1] = 'paper'
            else:
                getInfo('Provider (Velocity/Bungee/Waterfall)')
                if init_data[1].lower() != 'bungee' or init_data[1].lower() != 'waterfall':
                    init_data[1] = 'velocity'

            init_data.append(getInfo('Version (x.xx.x)'))
            

            init_data.append(getInfo('Auto restart on crash (Y/N)'))
            if init_data[3].lower() != 'n':
                init_data[3] = True
            else:
                init_data[3] = False

            print(init_data)
            
            

        else:
            c.print('[error]Unkown Command. try \'mserve help\' for help.[/]')
    print()

if __name__ == '__main__':
    mserve_exe()