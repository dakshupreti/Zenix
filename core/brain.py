from commands.search import search_command
from commands.memory import memory_command
from commands.calculator import calculator_command
from commands.browser import browser_command
from core.speaker import speak
from commands.open_apps import open_app
from commands.system import system_command

def think(command):
    command = command.lower()

    if open_app(command):
        return

    if system_command(command):
        return
    
    if memory_command(command):
        return
    
    if search_command(command):
        return
    
    if calculator_command(command):
        return
    
    if browser_command(command):
        return

    elif "how are you" in command:
        speak("I'm doing great. Ready to help you.")

    elif "who are you" in command:
        speak("I am Zenix, your personal AI assistant.")

    else:
        speak("Sorry, I don't know that command yet.")
