#
# https://neotap.net
# made with <3 from neo
#


import time
import typer
import webbrowser
from util import *
from rich.console import Console

mount = Console()
app = typer.Typer()



@app.command(short_help='links you to the docs')
def docs(open:bool = False):
    if open:
        webbrowser.open('https://docs.neotap.net/mserve')
    setInfo('\tYou can find the documentation here','https://docs.neotap.net/mserve')
    mount.print('\t[gray]use [cyan]--open[/] to open the link immediately')


# TODO add starterplugins and copy better default config files
@app.command(short_help='creates a new server')
def init(
    path:str = CD_CURRENT,
    version:str = '',
    provider:str = 'paper',
    ram:int = 2,
    autobackup:bool = True,
    autorestart:bool = True,
    # starterplugins:bool = True
    ):


    storageItems = {}
    providers = {
        'paper': 'servers, lightweight for effective servers.',
        'spigot': 'servers, the classic spigot with plugins.',
        'vanilla': 'vanilla, a normal MC server.',
        'waterfall': 'proxies, a better bungee proxy.',
        'bungee': 'proxies, a default proxy experience.',
        'velocity': 'proxies, a lightweight, advanced proxy.'
    }
    provider_type = 'servers'


    # path
    if not os.path.exists(path):
        os.makedirs(path)
    setInfo('Success',f'Found path at [green]{path}[/]','✔')


    # provider & version
    if provider not in providers:
        mount.print('\n[red bold]ERROR ➜ [/] Type needs one of:\n')
        for i in providers:
            mount.print(f'[green bold]{i.upper()}[/] - {providers[i]}')
    else: 
        for i in providers:
            if provider == i: 
                provider_type = providers[i].split(', ', 1)[0]
        download(
            f'https://serverjars.com/api/fetchJar/{provider_type}/{provider.lower()}/{version}',
            path,
            f'{provider.lower()}{version}.jar'
            )
        storageItems.update({'file': f'{provider.lower()}{version}.jar'})
    

    # ram
    if ram <= 0:
        setInfo('Error','[red]Please enter a ram amount greater than 1gb, set to 2gb.[/]','[red]✖[/]')
        storageItems.update({'ram': 2})
    elif ram > 10:
        setInfo('Error','[red]Please enter a ram amount less than 10gb, set to 2gb.[/]','[red]✖[/]')
        storageItems.update({'ram': 2})
    else: 
        storageItems.update({'ram': ram})
        setInfo('Success',f'Set ram dedication to [green]{ram}gb[/]','✔')


    # autobackup
    if autobackup:
        storageItems.update({'autobackup': True})
        setInfo('Success','Auto backup turned [green]on[/]','✔')
    

    # autorestart
    if autorestart:
        storageItems.update({'autorestart': True})
        setInfo('Success','Auto restart turned [green]on[/]','✔')


    # TODO starterplugins - runs download script, from the matching path of server (/assets/.../plugins.py)
    # if starterplugins:
    #     if os.path.exists(path):
    #         pass
    #     storageItems.update({'starterplugins': True})
    #     setInfo('Success','Starter plugins [green]added[/]','✔')

    storageAdd(path,storageItems)
    mount.print('\n[green bold]Initilization completed.[/]\nA failed download is most likely a faulty version.')



@app.command(short_help='starts a server or lists them')
def start(path:str = '.'):
    if not os.path.exists(path):
        raise Exception('path not found')
    if not os.path.exists(path + '/mserve.json'):
        raise Exception('mserve options not found (mserve.json)')

    storageItems = storageGet(path)

    if not os.path.isfile(path + '/' + storageItems["file"]):
        raise Exception('jarfile not found')
    
    mount.print('\n[green bold]STARTING SERVER[/]')
    setInfo('Path',path)
    setInfo('File',storageItems['file'])
    setInfo('Memory',str(storageItems['ram'])+'gb')
    if storageItems['autobackup']:backupWorlds(path)

    if 'autorestart' in storageItems or storageItems['autorestart']:
        while True:
            os.system(f'cd {path} & java -Xms{storageItems["ram"]}G -Xmx{storageItems["ram"]}G -jar {storageItems["file"]} --nogui')
            mount.print('[white]//////////////////////////////\ncut off thread[red bold]\n\nEXITED SERVER[/]\n\n[green]autorestarting in 5... (CTRL-C to cancel)[/]')

            if storageItems['autobackup']:backupWorlds(path)
            
            time.sleep(5)
    else:
        os.system(f'cd {path} & java -Xms{storageItems["ram"]}G -Xmx{storageItems["ram"]}G -jar {storageItems["file"]} --nogui')
        mount.print('[white]//////////////////////////////\ncut off thread[red bold]\n\nEXITED SERVER[/]')

        if storageItems['autobackup']:backupWorlds(path)



# TODO add loading backups, clearing backups
@app.command(short_help='backup a server\'s worlds (dirs including level.dat)')
def backup(path:str = '.'):
    if not os.path.exists(path):
        raise Exception('path not found')
    backupWorlds(path)


# TODO add mysql startup & kill all java instances
@app.command(short_help='other utilities')
def util():
    pass



if __name__ == '__main__':
    app()
