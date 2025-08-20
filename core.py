# core.py

from models.qwen import Qwen
from models.llama import Llama
from models.deepseek import DeepSeek

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

        self.ui.hacker_print(">>> Mark 1:", style="bold green")
        for token in generator:
            self.ui.hacker_print(token, delay=0.003, style="green")
        return ""
