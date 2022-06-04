
from random import choice
from pyttsx3 import init 
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import wikipedia 
import webbrowser

wikipedia.set_lang("it")
engine=init()
voices=engine.getProperty("voices")
engine.say("eccomi")
engine.runAndWait()
r=Recognizer()

with Microphone() as source:
    print("pronto ad ascoltare ")
    audio=r.listen(source)
    testo=r.recognize_google(audio, language="it-IT").lower()
    risposta="esprimiti meglio"
    print (testo)

    if"ricetta" in testo:
        risposta="non sono ancora in grado, però ti apro giallozafferano  "
        webbrowser.open("https://www.giallozafferano.it/")
    
    elif any(parola in testo for parola in["ore","ore","orario"]):
            risposta=f"sono le ore {datetime.now().strftime('%H e%M')}"
    
    elif "chi è" in testo:
            person =testo.replace("Chi è", '')
            risposta= wikipedia.summary(person, 2)
            print(risposta)
    
    elif "saluta" in testo:
        ogg=testo.replace("saluta", '')
        risposta = ("ciao "+ogg)
    
    elif "cos'è" in testo:
        ogg=testo.replace("cos'è", '')
        risposta= wikipedia.summary(ogg, 2)
        print(risposta)
    
    elif"dove si trova" in testo:
        risposta="cercatelo da solo"
        webbrowser.open ("https://www.google.com/maps/")
    
    elif "sasso carta forbice" in testo:
        engine.say("3")
        engine.runAndWait()
        engine.say("2")
        engine.runAndWait()        
        engine.say("1")
        engine.runAndWait()
        risposta= choice(["sasso","carta","forbice"])
    
    elif any(parola in testo for parola in["traduci","traducimi","tradurre"]):
        risposta="non sono brava in quella lingua"
        webbrowser.open ("https://translate.google.com/")
    
    elif"calcolatrice" in testo:
        risposta="ecco a te"
        webbrowser.open ("https://www.calcolatriceonline.it/")
    
    elif"amazon" in testo:
        risposta="ecco a te"
        webbrowser.open ("https://www.amazon.it/")
    
    elif"spotify" in testo:
        risposta="ecco a te"
        webbrowser.open ("https://open.spotify.com/")
    
    elif"netflix" in testo:
        risposta="ecco a te"
        webbrowser.open ("https://www.netflix.com/it/")
    
    engine.say(risposta)
    engine.runAndWait()   



