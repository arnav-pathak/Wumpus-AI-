import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

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
    command()

