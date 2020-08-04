import datetime
import os
import webbrowser

import pyttsx3  # convert text to speech
import speech_recognition as sr  # convert speech to text
import wikipedia

# for starting the speech to text
engine = pyttsx3.init('sapi5')  # supports nsss,
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# converting test to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning sir !')
    elif hour >= 12 and hour < 18:
        speak("Good evening sir!")
    elif hour >= 18 and hour < 24:
        speak("Good night sir! ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("cant recognize ....say that again")
        speak("cant recognize .... please, say that again")
        return 'none'
    return query


if __name__ == '__main__':
    Wishme()
    while True:
        query = takecommand().lower()
        if 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.com')
        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('gmail.com')
        elif 'start notepad' in query or 'open notepad' in query:
            speak('opening notepad')
            os.system('notepad.exe')
        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia...')
            speak(results)
        elif 'date' in query:
            date = datetime.datetime.today()
            speak(f"the date is {date}")
        elif 'time' in query:
            time = datetime.time.now().strftime("%H:%M:%S")
            speak(time)
        elif 'day' in query:
            day = datetime.datetime.today().weekday()
            dict = {0: 'monday', 1: 'tuesday', 3: 'wednesday', 4: 'thursday',
                    5: 'friday', 6: 'saturday', 7: 'sunday'}
            for i, j in dict.items():
                if i == int(day):
                    j = dict[i]
                    speak(f'the day is {day}')
        elif 'write in notepad' in query:
            speak('speak the content...')
            qt = takecommand()
            file = open('logs.txt', 'w+')
            while qt != 'stop writing':
                qt = takecommand()
                file.write(qt)
            file.close()
        if 'open word' in query:
            file=open(r'C:\Users\Meghansh Bansal\Desktop\untitled.docx', 'w')
            file.close()
            os.startfile(r'C:\Users\Meghansh Bansal\Desktop\untitled.docx')
            exit()
        elif 'quit' in query:
            speak("thank you, talk to you later!")
            exit()
