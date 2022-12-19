
import os
from rich import box
from rich.console import Console
from rich.table import Table

c = Console()
path = os.path.dirname(os.path.realpath(__file__))
line = '──────────────────────────────────────────────────────────────────────────────'
i = ''

while i != 'exit':
    c.print(f'\n[green bold]Starting {path}...[/]\n{line}')

    os.system('java -Xms512M -Xmx512M -jar BungeeCord.jar')

    c.print(f'{line}\n[red bold]//////////////////////////////\ncut off thread - type \'exit\' to close.\nEXITED SERVER\n[/]')
    i = input()
