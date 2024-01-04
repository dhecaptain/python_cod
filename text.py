
import pyttsx3
engine=pyttsx3.init()

def speak(n):
    engine.say(n)
    print(n)
    engine.runAndWait()

while True:
    text=input("Enter a n or a character that you want the engine to say(or enter exit to quit: ")
    if text.lower()=='exit':
        break
    speak(text)    