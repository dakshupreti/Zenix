from core.speaker import speak

print("Calculator module imported")

def calculator_command(command):
    print("Calculator received:", command)

    command = command.lower()

    if command.startswith("calculate "):
        print("Inside calculate block")

        query = command.replace("calculate ", "")

        try:
            answer = eval(query)
            print("Answer:", answer)
            speak(f"The answer is {answer}")

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I couldn't calculate that.")

        return True

    return False