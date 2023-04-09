
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyjokes
import pywhatkit
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir!")

def time():
    hour = str(datetime.datetime.now().hour)
    min = str(datetime.datetime.now().minute)
    s = hour + ":" + min
    return s

def age():
    dob = "2023-02-24"
    dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d')
    age = datetime.datetime.now() - dob_date
    age_in_days = int(age.days)
    return age_in_days

def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if 'name' in query:
            speak("My name is David")
        elif 'age' in query or 'old' in query:
            d = age()
            speak(f"My age is {d} days")
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
        elif 'search' in query:
            query = query.replace("search", "")
            speak(f"Searching for {query} on the web...")
            pywhatkit.search(query)
        elif 'how are you' in query:
            speak('I am fine, thank you!')
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
        elif 'tell me the time' in query:
            t = time()
            speak(f"The time is {t}")
        elif 'joke' in query:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            speak(joke)
