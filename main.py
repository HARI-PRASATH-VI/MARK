from ui import UI
from core import Assistant

def main():
    ui = UI()
    assistant = Assistant(ui)

    ui.banner()

    while True:
        try:
            user_input = ui.get_user_input()
            if user_input.lower() in ["exit", "quit"]:
                ui.display_response("Goodbye, Hacker 🚀")
                break
            # streaming is already handled inside core.py
            assistant.handle(user_input)
        except KeyboardInterrupt:
            ui.display_response("[!] Session terminated.")
            break

if __name__ == "__main__":
    main()
