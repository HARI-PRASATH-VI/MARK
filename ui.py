from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
import time

class UI:
    def __init__(self):
        self.console = Console()

    def banner(self):
        self.console.print(
            Panel(
                "[bold green]Welcome to MARK 1 - Retro Hacker Assistant[/bold green]",
                border_style="green",
                padding=(1, 2)
            )
        )

    def hacker_print(self, text, delay=0.00, style="bold green"):
        for char in text:
            self.console.print(char, style=style, end="")
            time.sleep(delay)
        self.console.print()

    def get_user_input(self):
        return self.console.input("[bold cyan]>>> You: [/bold cyan]")

    def display_response(self, text):
        self.console.print(
            Panel(text, title="[bold green]Mark 1[/bold green]", border_style="green"),
            justify="middle"
        )

    def display_code(self, code, lang="python"):
        syntax = Syntax(code, lang, theme="monokai", line_numbers=True, word_wrap=True)
        self.console.print(
            Panel(
                syntax,
                title="[bold cyan]💻 MARK 1 Code Box[/bold cyan]",
                border_style="bright_green",
                padding=(1, 2)
            ),
            justify="center"
        )
