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
from Camera import camera





print("Loading your AI personal assistant-Jake")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")




def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

    try:
      statement = r.recognize_google(audio, language='en-in')
      print(f"User said:{statement}\n")

    except Exception as e:
      speak("Pardon me, please say that again")
      return "None"
    return statement

def NewsFromBBC():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    # to read the news out loud
    speak(results)
    time.sleep(3)



speak("Loading your AI personal assistant-Lily")
wishMe()

if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you ?")
        statement = takeCommand().lower()

        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("your personal assistant-Jake is shutting down,Good bye")
            print("your personal assistant-Jake is shutting down,good bye")
            break

        if "wikipedia" in statement:
            speak("Searching Wikipedia...")
            statement = statement.replace("wikipedia", "")
            result = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in statement:
            webbrowser.open_new_tab('https://www.youtube.com')
            speak("youtube is open now")
            time.sleep(5)

        elif "open google" in statement:
            webbrowser.open_new_tab('https://www.google.com')
            speak("Google chrome is open now")
            time.sleep(5)

        elif "open gmail" in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:

            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x['cod'] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]['description']
                speak("Temperature in kelvin unit is " + str(current_temperature) +
                      "\nHumidity in percentage is " + str(current_humidity) +
                      "\nDescription " + str(weather_description))
                print("Temperature in kelvin unit = " +
                      str(current_humidity) +
                      "\nHumidity in percentage = " +
                      str(current_humidity) +
                      "\nDescription = " + str(weather_description))

            else:
                speak("City not found")


        elif 'time' in statement:
            x_time = datetime.datetime.now().strftime("%d-%b-%Y %I.%M %p")
            speak(f"the time is {x_time}")
            print(f"The time is {x_time}")

        elif 'today date' in statement:
            strDate = datetime.datetime.now().strftime('%A')
            speak(f'today date is {strDate}')

        elif "who are you " in statement or 'what can you do' in statement:
            speak("I am Jake version 1 point 0 your personal assistant . I am programmed to minor tasks like"
                  'open youtube,google chrome,gmail and stackoverflow, predict time, take a photo,search wikipedia,predict weather'
                  'in different cities, get top headline news from time of united states and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who create you" in statement:
            speak("I was built by J")
            print("I was built by J")
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is stackoverflow")

        elif "news" in statement or "what news today" in statement:
            NewsFromBBC()


        elif 'reading' in statement or "read somethings" in statement:
            news = webbrowser.open_new_tab("https://www.bloomberg.com")
            speak("Here are some headlines from bloomberg,happy reading")
            time.sleep(6)
        elif "camera" in statement or "take a photo" in statement:
            camera.VideoCapture()

        elif "search" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "calculation" in statement:
            speak("I can answer to computational and geographical questions and what question do you want to ask now")
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client("R2K75H-7ELALHR35X")
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("ok, your pc will log off in 10 seconds make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)



