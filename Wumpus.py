import pyttsx3
import datetime

def speak(audio):
       pass      

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voice[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

if __name__=="__main__" :
    speak("Code With Harry")

 
