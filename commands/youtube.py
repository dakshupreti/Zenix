import webbrowser
from urllib.parse import quote_plus
from core.speaker import speak

def youtube_command(command):
    command = command.lower()

    if command.startswith("youtube "):
        query = command.replace("youtube ", "")

        url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"

        speak(f"Opening youtube for {query}")

        webbrowser.open(url)

        return True
    
    return False