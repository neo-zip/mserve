#
# https://neotap.net
# MIT licence: made with <3 from neo
#


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



@app.command(short_help='creates a new server')
def init(
    path:str = CD_CURRENT,
    version:str = '',
    provider:str = 'paper',
    ram:int = 2,
    autobackup:bool = True,
    autorestart:bool = True
    ):

    if not os.path.exists(path):
        os.makedirs(path)
    setInfo('Success',f'Found path at [green]{path}[/]','✔')

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
    
    if ram <= 0:
        setInfo('Error','[red]Please enter a ram amount greater than 1gb, set to 2gb.[/]','[red]✖[/]')
        storageItems.update({'ram': 2})
    elif ram > 10:
        setInfo('Error','[red]Please enter a ram amount less than 10gb, set to 2gb.[/]','[red]✖[/]')
        storageItems.update({'ram': 2})
    else: 
        storageItems.update({'ram': ram})
        setInfo('Success',f'Set ram dedication to [green]{ram}gb[/]','✔')

    if autobackup:
        storageItems.update({'autobackup': True})
        setInfo('Success','Auto backup turned [green]on[/]','✔')
    
    if autorestart:
        storageItems.update({'autorestart': True})
        setInfo('Success','Auto restart turned [green]on[/]','✔')

    storageAdd(path,storageItems)
    mount.print('\n[green bold]Initilization completed.[/]\nA failed download is most likely a faulty version.')


@app.command(short_help='starts a server or lists them, "all" selector works')
def start(server:str):
    if server == 'all':
        mount.print('STARTING ALL SERVERS')
    else:
        mount.print(f'just starting {server}')



@app.command(short_help='backs up a server\'s worlds (world_*), "all" selector works')
def backup(server:str):
    typer.echo(f'adding DFSADSFASD to {server}')
    print(CD_FILE)
    os.system('java -Xms1G -Xmx1G -jar spigot-1.18.2.jar --nogui')



@app.command(short_help='other utilities')
def util():
    storageAdd(CD_CURRENT,{'test':'okay'})
    storageGet(CD_CURRENT,'test')





if __name__ == '__main__':
    app()



# init_data = [{}]

# mount.print('[magenta bold]INITILIZATION[/]\n[data]options to setup a new sever\nand dont worry, you can change most options later. \n[bold green]Press enter to skip (sets default)[/]')

# init_data.append(getInfo('Path (skip to set current dir/...)'))
# if init_data[0] == '':
#     init_data[0] = cd_current
# elif not os.path.exists(init_data[0]):
#     os.makedirs(init_data[0])


# init_data.append(getInfo('Type (Normal/Proxy)'))
# if init_data[1].lower() != 'proxy':
#     getInfo('Provider (Paper/Sigot/Vanilla)')
#     if init_data[1].lower() != 'vanilla' or init_data[1].lower() != 'spigot':
#         init_data[1] = 'paper'
# else:
#     getInfo('Provider (Velocity/Bungee/Waterfall)')
#     if init_data[1].lower() != 'bungee' or init_data[1].lower() != 'waterfall':
#         init_data[1] = 'velocity'

# init_data.append(getInfo('Version (x.xx.x)'))


# init_data.append(getInfo('Auto restart on crash (Y/N)'))
# if init_data[3].lower() != 'n':
#     init_data[3] = True
# else:
#     init_data[3] = False

# print(init_data)



# mount.print('[error]Unkown Command. try \'mserve help\' for help.[/]')