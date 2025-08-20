# models/deepseek.py

import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

class DeepSeek:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "deepseek/deepseek-r1:free"

    def generate_stream(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "Mark1 Assistant",
            "Accept": "text/event-stream",
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are Mark 1, a coding assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 512,
            "temperature": 0.2,
            "stream": True
        }

        with requests.post(self.url, headers=headers, json=payload, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    decoded = line.decode("utf-8")
                    if not decoded.startswith("data: "):
                        continue
                    data = decoded[6:]
                    if data.strip() == "[DONE]":
                        break
                    try:
                        content = json.loads(data)
                        delta = content["choices"][0]["delta"].get("content", "")
                        if delta:
                            yield delta
                    except json.JSONDecodeError:
                        continue
