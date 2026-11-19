import speech_recognition as Ak

import pyttsx3



recognize = Ak.Recognizer()

bol = pyttsx3.init()

def speak(text):
    bol.say(text)
    bol.runAndWait()

if __name__ == "__main__":
    speak("Hello,I M Rabta")

while True:
        # obtain audio from the microphone

    # recognize speech using
    R = Ak.Recognizer()
    print("recognizing")
    commands = ""
    try:
        with Ak.Microphone() as src:
            print("Listening...")
            audio = R.listen(src)
        word = R.recognize_google(audio)
        if(word.lower == "Megha"):
            speak("yes")
        with Ak.Microphone() as src:
            print("Activated...")
            audio = R.listen(src)
            commands = R.recognize_google(audio)
    except Ak.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except Ak.RequestError as e:
        print("Google error; {0}".format(e))

    if "only stop" in commands or "exit from terminal" in commands :
        speak("Goodbye! i am going .")
        break
