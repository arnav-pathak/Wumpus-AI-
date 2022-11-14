import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os



def speak(audio):
       pass      

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def welcomeme():
    time = int (datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("Good Morning! Matrix Here")

    elif time>=12 and time<18:
        speak("Good Afternoon! Matrix Here")

    else:
        speak("Good Evening! Matrix Here")

    speak("How May I Help you?")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Identifying.....")
        query = r.recognize_google(audio, Language="en-in")
        print(f"You said: {query}\n")


    except Exception as e:
        print("Please say again.")
        return "None"
    return query









if __name__=="__main__" :
    welcomeme()
    while  True:
        query = command().lower()

        if 'wikipedia' in query:
            speak("Searching..")
            query = query.replace("wikiepdia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("As per Wikipedia")
            speak(results)

        elif 'search youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search creator' in query:
            webbrowser.open("https://github.com/Varietyop/Varietyop")
        
        elif 'search outlook' in query:
            webbrowser.open("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1668442957&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d125a4b57-538d-bf9c-e7b8-531a68c90846&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
        
        elif 'tell time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")

        elif 'tell about updates' in query:
            speak("We are currently developing Matrix 2.0 with a GUI interface.")

        elif 'open code' in query:
            codePath = "C:\Users\sacpa\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        
        elif 'open chrome' in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)

        elif 'open Blender' in query:
            blendPath = "C:\Program Files\Blender Foundation\Blender 3.3\blender-launcher.exe"
            os.startfile(blendPath)

 

            


