import speech_recognition as sr

def recognise():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите что-нибудь!")
        audio = r.listen(source)

    return r.recognize_google(audio, language="ru")  

print(recognise())
