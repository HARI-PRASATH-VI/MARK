# core.py

from models.qwen import Qwen
from models.llama import Llama
from models.deepseek import DeepSeek
import sys, time

class Assistant:
    def __init__(self, ui):
        self.ui = ui
        self.qwen = Qwen()
        self.llama = Llama()
        self.deepseek = DeepSeek()

    def handle(self, user_input: str) -> str:
        # Routing logic:
        if "explain" in user_input.lower():
            generator = self.llama.generate_stream(user_input)
        elif "code" in user_input.lower() or "function" in user_input.lower():
            generator = self.deepseek.generate_stream(user_input)
        else:
            generator = self.qwen.generate_stream(user_input)

        # Streaming response
        self.ui.console.print("[bold green]Mark 1:[/bold green] ", end="")
        sys.stdout.flush()

        response = ""
        for token in generator:
            response += token
            # print inline without line breaks
            print(token, end="", flush=True)
              # small delay for typing effect

        print()  # final newline after response
        return response
