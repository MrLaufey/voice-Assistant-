import speech_recognition as sr
import pyttsx3
import datetime
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time

MASTER ='sir'

print('intializing mike')

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices','voices[0].id')
#print(voices[0].id)

def speak(text):
  engine.say(text)
  engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("Good morning" + MASTER)

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good evening" + MASTER)

    speak("yo i am mike whatsup how may i help you?")


wishMe()


