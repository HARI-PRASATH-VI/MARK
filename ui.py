from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
import time

class UI:
    def __init__(self):
        self.console = Console()

    def banner(self):
        self.console.print(
            Panel("[bold green]Welcome to MARK 1 - Retro Hacker Assistant"),
            style="bold green"
        )

    def hacker_print(self, text, delay=0.01, style="bold green"):
        for char in text:
            self.console.print(char, end="", style=style, justify="left")
            time.sleep(delay)
        self.console.print()

    def get_user_input(self):
        return self.console.input("[bold cyan]>>> You: [/bold cyan]")

    def display_response(self, text):
        self.console.print(
            Panel(text, title="[bold green]Mark 1[/bold green]")
        )

    def display_code(self, code, lang="python"):
        syntax = Syntax(code, lang, theme="monokai", line_numbers=True)
        self.console.print(Panel(syntax, title="[bold green]Code[/bold green]"))
