import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime  
import wikipedia

global query
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything : ')
        r.pause_threshold=0.7
        audio=r.listen(source)
        try:
            global query
            query=r.recognize_google(audio,language ='en-in')
            print('You said : {}'.format(query))
        except:
            speak('Sorry could not hear you.!')
    return query


def speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()
    
def tellTime():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir " + hour + "Hours and" + min + "Minutes")
    
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

            
def Hello():
    speak("hello sir i am Joe. Tell me how may I help You")

    
def Take_query():
    Hello()
    while(True):
        query=takeCommand().lower()
        if "open google" in query:
            speak("Opening google")
            webbrowser.open("www.google.com")
            continue
        
        elif "open youtube" in query:
            speak("opening Youtube")
            webbrowser.open("www.youtube.com")
            continue
            
        elif "time" in query:
            tellTime()
            continue
        
        elif "day" in query:
            tellDay()
            continue
        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(result)
            speak(result)
            
        elif "good bye" or "goodbye"in query:
            speak("Bye. Thank you for interacting See you soon again.")
            exit()
             
if __name__=='__main__':
    Take_query()
