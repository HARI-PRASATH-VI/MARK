import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

class Llama:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        # You can switch size if needed (8B, 70B, etc.)
        self.model = "meta-llama/llama-3.1-70b-instruct"

    def generate_stream(self, prompt: str):
        """
        Yields tokens from OpenRouter (LLaMA 3.1) as they arrive.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http://localhost:8000",  # required by OpenRouter
            "X-Title": "Mark1 Assistant",
            "Accept": "text/event-stream",
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are Mark 1, a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 512,
            "temperature": 0.3,
            "stream": True
        }

        with requests.post(self.url, headers=headers, json=payload, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    try:
                        if line.startswith(b"data: "):
                            data = line.decode("utf-8")[6:]
                            if data.strip() == "[DONE]":
                                break
                            content = json.loads(data)
                            delta = content["choices"][0]["delta"].get("content", "")
                            if delta:
                                yield delta
                    except Exception:
                        continue
