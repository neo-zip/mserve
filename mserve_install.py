#
# https://neotap.dev
# MIT licence: made with <3 from neo
#


# import os
# import time
import typer
# from rich import box
from rich.console import Console
# from rich.table import Table
from rich.highlighter import RegexHighlighter
from rich.theme import Theme



class synLight(RegexHighlighter):
    highlights = [r'1234567890.']
c = Console(highlighter=synLight(), theme=Theme({
    'low_success': 'green',
    'link': 'cyan'
}))
app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")



if __name__ == '__main__':
    app()
