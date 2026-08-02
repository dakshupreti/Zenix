from core.brain import think

print("Starting Zenix...")
print("Type 'exit' to quit.\n")

while True:
    command = input("You: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    think(command)