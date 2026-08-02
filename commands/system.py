from datetime import datetime
from core.speaker import speak


def system_command(command):
    command = command.lower()

    if "time" in command:
        current = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current}")
        return True

    if "date" in command:
        today = datetime.now().strftime("%d %B %Y")
        speak(f"Today is {today}")
        return True

    return False