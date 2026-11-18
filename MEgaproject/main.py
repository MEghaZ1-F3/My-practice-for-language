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



