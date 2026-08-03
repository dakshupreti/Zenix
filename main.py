from core.brain import think
from core.startup import startup

startup()

print("Type 'exit' to quit.\n")

while True:
    command = input("You: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    think(command)