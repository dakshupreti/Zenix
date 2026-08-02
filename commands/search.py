import webbrowser
from urllib.parse import quote_plus
from core.speaker import speak


def search_command(command):
    command = command.lower()

    if command.startswith("search "):
        query = command.replace("search ", "")

        url = f"https://www.google.com/search?q={quote_plus(query)}"

        speak(f"Searching Google for {query}")

        webbrowser.open(url)

        return True

    return False