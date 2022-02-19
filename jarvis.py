import pyttsx3
import speech_recognition as sr
import date-time
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0])

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0  and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("hello sir i am jarvis your personal assistant. please tell me how can i help you")







if __name__== "__main__":
    wish()
while True:

    if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Ado 0be\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play musi" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))



        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")



        elif "play songs on youtube" in query:
            kit.playonyt("Kabhii Tumhhe –Official Video")



        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak ("sir, do have any other work")


        



