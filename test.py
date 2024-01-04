import speecher as sr

r=sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice_data=""
        try:
            voice_data=r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("sorry i did not get that")
        except sr.RequestError:
            print("sorry, my speech service is down")
        return voice_data
    
print("How can I help you?")
voice_data =record_audio()
print(voice_data)