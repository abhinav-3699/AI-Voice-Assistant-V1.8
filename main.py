import pyttsx3
import speech_recognition as sr
import datetime 
import pywhatkit
import wikipedia as sk
import webbrowser
import pyautogui
import time
import wolframalpha 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding....")
        queri = r.recognize_google(audio,language='en-in')
        print(f"You Said : {queri}")

    except Exception as e:
        return "None"
    
    return queri

current_time = datetime.datetime.now()
hour = current_time.hour
min = current_time.minute
final_time = (hour, min)

def greet_me():
    if hour>=0 and hour<12 :
        speak(f"Good morning sir, its {final_time}A,M, how can i assist you")
    elif hour>=12 and hour<16:
        speak(f"Good afternoon sir, its {final_time}P,M, how can i assist you")
    elif hour>=16 and hour<18:
        speak(f"Good evening sir, its {final_time}P,M, how can i assist you")
    else :
        speak(f"Welcome back sir, its {final_time}P,M, how can i assist you")
    return 

def googleScrap(query):
    speak("This is what i found on google")
    query = query.replace("google","")
    try:
        time.sleep(0.5)
        pywhatkit.search(query)
        result = sk.summary(query,1)
        speak(result)

        

    except : 
        speak("No speakable output found")

    return 





    
if __name__ == "__main__":
    greet_me()
    while True:
        query = command().lower()
        if "how are you" in query:
            speak("i am fine sir, how are you")

        
        elif "google" in query:
            googleScrap(query)
        
        
        elif "open instagram" in query:
            speak("Opening instagram")
            
            webins = "https://www.instagram.com/"
            time.sleep(0.5)
            webbrowser.open(webins)

        elif "open gmail" in query:
            speak("Opening mail")
            webmail = "https://mail.google.com/mail/u/0/#inbox"
            time.sleep(0.5)
            webbrowser.open(webmail)

        elif "open google" in query:
            speak("Opening google")
            webgoogle = "https://www.google.com/"
            time.sleep(0.5)
            webbrowser.open(webgoogle)

        elif "open youtube" in query:

            speak("Opening youtube ")
            webyoutube = "https://www.youtube.com/"
            time.sleep(0.5)
            webbrowser.open(webyoutube)

        elif "summarise" in query:
            text_summarization(query)
        
        elif "close it" in query:
            pyautogui.hotkey("ctrl","w")
        elif "close" in query:
            pyautogui.hotkey("ctrl","w")
        
        elif "close all tabs" in query:
            speak("On your mark sir")
            pyautogui.hotkey("ctrl","shift","w")
        
        
        elif "run" in query:
            pyautogui.hotkey("windows key","r")
        
        elif "open github" in query:
            speak("Opening github ")
            time.sleep(0.5)
            wbegithub = "https://github.com/"
            webbrowser.open(wbegithub)
        elif " open my github profile" in query:
            webbrowser.open("https://github.com/abhinav-3699")

    

            



        elif "go to sleep" in query:
            speak("I hope it helped ")
            break
        elif "exit" in query:
            speak("I hope it helped ")
            break


