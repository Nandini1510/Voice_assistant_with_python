# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello Nandini,Good Morning")
        print("Hello Nandini,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello Nandini,Good Afternoon")
        print("Hello Nandini,Good Afternoon")
    else:
        speak("Hello Nandini,Good Evening")
        print("Hello Nandini,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration =1)
        print("Listening....")
        audio=r.listen(source)
        
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Please say that again")
            return "None"
        return statement
    print("Loading your AI assistant")
    speak("Loading your AI assistant")
    wishMe()
    

if __name__=='__main__':
    wishMe()
    while True:
        speak("How can i help you today?")
        statement=takeCommand().lower()
        if statement==0:
            continue
        
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("AI shutting down, bye!")
            print("AI shutting down, bye!")
            break
        
        if 'wikipedia' in statement:
            speak("Searching wikipedia...")
            statement=statement.replace("wikipedia", "")
            results=wikipedia.summary(statement,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
              
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Welcome to youtube")
            time.sleep(5)
        
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google open now")
            time.sleep(5)
            
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
            
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
     
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="WXPHPP-G8UAKT9KTR"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Nandini")
            print("I was built by Nandini")
            
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
    time.sleep(5)
