import pyttsx3
import datetime
import speech_recognition as spr
import wikipedia
import webbrowser
import os
import pyautogui
import time
#spotify experiment
#setting of voice 
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#def send_msg(to, content):
    #pywhatkit.sendwhatmsg('+919565167934','mummy thodi der mai call karte hain ','12','35')
#setting up audio of jarvis
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#functions    
def wishme():
    hour =int( datetime.datetime.now().hour ) 
    if hour >= 5 and hour <12:
        speak("GOOD MORNING ")
    elif hour >= 12  and hour <16:
        speak("good afternoon folks")
    else:
     speak("Good evening")
    speak("i am there to assist you , HOW MAY I HELP YOU !?")               
def takecommand():
    r = spr.Recognizer()
    with spr.Microphone() as source:
        print("Listening............")
        r.pause_threshold = 1.1
        r.energy_threshold = 100
        audio  = r.listen(source)
    try:
        print("Recognizing............")
        query  = r.recognize_google(audio , language ='en-in')
        print("user said:", {query})
    except Exception as e:
     
        print("say that again please .........")
        
        return "None"     
    return query
#main logics and task             
if __name__ == '__main__':
    wishme()
    while True:
     query = takecommand().lower()
     if 'wikipedia' in query :
        speak("Searching Wikipedia....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)

     elif 'open youtube' in query :
        webbrowser.open ("http://www.youtube.com")

     elif 'open Google' in query :
        webbrowser.open ("http://www.google.com")

        
     ########    spotify fun {} -> ############

     elif 'open spotify' in query :
        os.startfile("C:\\Users\\asus\\AppData\\Roaming\\Spotify\\Spotify.exe")
        speak("which song to play ....")
        query  = takecommand().lower()
        os.system('spotify')
        time.sleep(5)
        pyautogui.hotkey('ctrl','l')
        pyautogui.write(query,interval=0.1)
        for key in ['enter','pagedown','tab', 'enter','enter']:
          time.sleep(2)
          pyautogui.press(key)


     elif 'open codechef' in query :
        webbrowser.open ("https://www.codechef.com/")   

        
     elif 'time' in query :
        strtime = datetime.datetime.now().strftime("%H-%M-%S")
        speak("master the time is {strtime}")
     elif 'discord' in query :  
        codepath =  "C:\\Users\\asus\\AppData\\Local\\Discord.exe"
        os.startfile(codepath)
     elif 'code' in query :  
        codepath =  "C:\\Users\\asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        os.startfile(codepath)   
     elif 'open whatsapp' in query:
            webbrowser.open ("https://web.whatsapp.com/")  
     #elif 'mail' :
            #webbrowser.open ("https://mail.google.com/mail/u/0/#inbox")  
     elif 'open twitter'  in query :
        webbrowser.open ("https://twitter.com/home") 
                
     elif 'quit ' in query:
        exit()                      


    