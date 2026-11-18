import speech_recognition as Ak
import webbrowser
import pyttsx3



recognizer = Ak.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, your assistance")

while True:
        # obtain audio from the microphone
    r = Ak.Recognizer()
    with Ak.Microphone() as src:
        print("Listening...")
        audio = r.listen(src)

    # recognize speech using Sphinx
    try:
        commands = r.recognize_sphinx(audio)
        print(commands)
    except Ak.UnknownValueError:
        print("Sphinx could not understand audio")
    except Ak.RequestError as e:
        print("Sphinx error; {0}".format(e))

