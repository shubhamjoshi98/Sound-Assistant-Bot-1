# open in pycharm community --- completed
import pyttsx3
import os
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import datetime
import speech_recognition as sr
import datetime
import random
from tkinter import *
import psutil

engine = pyttsx3.init()
voices=engine.getProperty('voices')
#print(voices[0])
engine.setProperty('voice',voices[0].id)

def WishMe():
    ''' Wish according to datetime'''
    hour= int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("Good Morning !!")
    elif (hour>=12 and hour<18):
        speak("Good Afternoon !!")
    else:
        speak("Good Evening !!")

    speak("May I help you ?")



def takeCommand():
    '''Microphone input to string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold =1
        audio= r.listen(source)

    try:
        print("Recognizing ...")
        query =r.recognize_google(audio,language="en-in")
        print("user said -",query)
        return query

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return("none")

def speak(audio):
    '''speak audio'''
    engine.say(audio)
    engine.runAndWait()
    pass

def SendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587) #587 is port
    server.ehlo()
    server.starttls()

    file1 = open("pass.txt", "r")
    password=file1.readline() # save your email ids password in a txt file named pass.txt
    id='adarshagrawal4@gmail.com' # my email id change accordingly
    server.login(id,password)
    server.sendmail(id,to,content)
    server.close()
    file1.close()
    
def speakConvertedTime(seconds):
    ''' convert seconds to hrs : min : sec and speak the result '''
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print("The battery will last: " + "%d:%02d:%02d" % (hours, minutes, seconds))
    return speak(f"Battery will last for about {hours} hour, {minutes} minutes and {seconds} seconds")

if __name__ == "__main__":
    WishMe()
    count=0
    while True:
        query=takeCommand().lower()
        #logic for executing task--
        if 'wikipedia' in query:
            speak('Searching'+query+'in wikipedia')
            query=query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'change speaker' in query:
            speak("Sure Nice to have you")
            i=random.randint(0,40)
            engine.setProperty('voice', voices[i].id)
            speak("Changed speaker successfully"+"I am "+ voices[i].name +" Nice to meet you !")

        elif 'open youtube' in query:
            speak("Sure")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Sure")
            webbrowser.open("https://www.google.com")

        elif 'codeforces contest' in query:
            speak("Sure")
            webbrowser.get('chrome').open("https://www.codeforces.com")
            webbrowser.open("https://10xiitian.ibhubs.co/code-playground")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H %M")
            speak("The time is" + strTime)

        elif 'music' in query:
            speak("Sure")
            url="//Applications"
            os.system("open //Applications//Spotify.app")

        elif ('bye' in query) or ('thank' in query):
            speak('okay Bye')
            break
        elif 'email' in query:
            #email ids of targets stored in dictionary--
            d={'adarsh':"adarsh.adarsh.agrawal@gmail.com",'divya':"divyaagrawal8484@gmail.com"}
            try:
                speak("Whom to send Email Adarsh ?")
                name= takeCommand().lower()
                to = d[name]
                speak("What to write in Email ?")
                content =takeCommand()
                SendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Cant send Email now")
                
        elif 'shut down' or 'shutdown' in query:
            speak("Are you sure that you want to shut down your PC? Say only YES or NO")
            confirmation = takeCommand().lower()
            if confirmation != 'yes':
                exit()
            else:
                speak("System is shutting down")
                os.system("shutdown /s /t 1")
                
        elif 'restart' in query:
            speak("Are you sure that you want to restart your PC? Say only YES or NO")
            confirmation = takeCommand().lower()
            if confirmation != 'yes':
                exit()
            else:
                speak("System is restarting")
                os.system("shutdown /r /t 1")
                
        elif 'battery' in query:
            battery = psutil.sensors_battery()
            battery_percent = battery.percent
            battery_state = battery.power_plugged
            if battery_state == True:
                speak(f"The battery is {battery_percent} percent and is charging")
            else:
                speak(f"The battery is {battery_percent} percent ")
                battery_time_left = int(battery.secsleft)
                speakConvertedTime(battery_time_left)        
                
        elif query=='':
            count=count+1
            speak("I am not getting any response from your side . Say Bye to exit")

        else:
            speak("I cant answer your query right now")

        if (count>=3):
            speak("Okay Bye for now ")
            break
    pass
