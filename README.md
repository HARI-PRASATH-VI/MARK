# Mark v1 🤖💻
> Retro Hacker-Style Coding Assistant (Terminal UI + OpenRouter Models)

Mark v1 is a **voice/code assistant** with a terminal retro look, built using:
- [Rich](https://github.com/Textualize/rich) for the hacker-style UI
- [OpenRouter](https://openrouter.ai/) for free & open-source AI models
  - Qwen for coding
  - LLaMA for explanations
  - DeepSeek for reasoning

---

## 🚀 Features
- Hacker-style terminal output with Rich
- Hybrid model approach (Qwen + LLaMA + DeepSeek)
- API streaming responses
- Extensible modular design (`main.py`, `core.py`, `ui.py`, `models/`)

### project structure

mark1/
│── main.py # Entry point
│── core.py # Assistant logic & routing
│── ui.py # Retro hacker UI
│── models/ # Qwen, LLaMA, DeepSeek APIs
│── .env # 🔒 Your API key (ignored by Git)
│── requirements.txt
│── README.md

# cloning the repo

## 🔑 Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/HARI-PRASATH-VI/mark.git
   cd mark
2. pip install -r requirements.txt
3. OPENROUTER_API_KEY=your_openrouter_api_key_here free open router models only included
4. python main.py
 
# Requirements
see requirements.txt





