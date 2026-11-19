import speech_recognition as Ak

import pyttsx3



recognizer = Ak.Recognizer()

bol = pyttsx3.init()

def speak(text):
    bol.say(text)
    bol.runAndWait()

if __name__ == "__main__":
    speak("Hello,I M Rabta")

while True:
        # obtain audio from the microphone
    r = Ak.Recognizer()
    with Ak.Microphone() as src:
        print("Listening...")
        audio = r.listen(src)

    # recognize speech using
    try:
        commands = r.recognize_google(audio)
        print(commands)
    except Ak.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except Ak.RequestError as e:
        print("Google error; {0}".format(e))

    if "only stop" in commands or "exit from terminal" in commands :
        speak("Goodbye! .")
        break
