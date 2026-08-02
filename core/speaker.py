import pyttsx3


def speak(text):
    print("Zenix:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 180)

    engine.say(text)
    engine.runAndWait()

    engine.stop()