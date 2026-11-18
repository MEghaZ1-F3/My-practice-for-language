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




