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
                ui.hacker_print("Goodbye, Hacker 🚀")
                break
            response = assistant.handle(user_input)
            ui.display_response(response)
        except KeyboardInterrupt:
            ui.hacker_print("\n[!] Session terminated.")
            break

if __name__ == "__main__":
    main()
