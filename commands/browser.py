import pywhatkit
import webbrowser
from core.speaker import speak


def browser_command(command):
    command = command.lower()

    if command.startswith("search "):
        query = command.replace("search ", "")

        speak(f"Searching Google for {query}")
        pywhatkit.search(query)

        return True

    elif command.startswith("youtube "):
        query = command.replace("youtube ", "")

        speak(f"Playing {query} on YouTube")
        pywhatkit.playonyt(query)

        return True

    elif command.startswith("open website "):
        website = command.replace("open website ", "")

        speak(f"Opening {website}")

        webbrowser.open(f"https://{website}")

        return True

    return False