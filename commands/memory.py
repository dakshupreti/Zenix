def memory_command(command):
    

    command = command.lower()

    if command.startswith("remember "):
        

        text = command.replace("remember ", "")

        if " is " not in text:
            speak("Please say: remember something is something.")
            return True

        key, value = text.split(" is ", 1)

        

        remember(key, value)

        speak("I'll remember that.")

        return True

    if command.startswith("what is "):
        

        key = command.replace("what is ", "")

        value = recall(key)



        if value:
            speak(f"{key} is {value}")
        else:
            speak("I don't remember that.")

        return True

    return False