import os
from core.speaker import speak

def open_app(command):
    command = command.lower()

    if "chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("start calc")

    else:
        return False

    return True