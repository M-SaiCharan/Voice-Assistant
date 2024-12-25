import os
import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime
import winsound
import time as t
from countries import countries 

sound_folder = os.path.join(os.getcwd(), "sounds")

engine = pyttsx3.init()

def speak(keyword):
    engine.say(keyword)
    engine.runAndWait()

def play_sound(filename):
    try:
        sound_path = os.path.join(sound_folder, filename)
        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print(f"Failed to play sound: {e}")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        play_sound('active.wav')
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language="en-IN")
            play_sound('success.wav')
            t.sleep(0.3)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            play_sound('fail.wav')
            return ""
        except sr.RequestError:
            speak("There was a problem with the speech recognition service.")
            return ""
        except Exception as e:
            print(f"Listening error: {e}")
            return ""

def get_weather(city):
    api_key = "01ec37f4924f4fefb87165808240812"  # Replace with your WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        data = response.json()
        if "current" in data:
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            print(f"The weather in {city} is {condition} with a temperature of {temp} °C.")
            speak(f"The weather in {city} is {condition} with a temperature of {temp} degrees Celsius.")
        else:
            print("Error fetching weather data. Please check your API key or city name.")
            speak("Error fetching weather data. Please check your API key or city name.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak(f"An error occurred: {e}")

def get_news(keyword=None):
    api_key = "53bc69bee91a4fefaa6de41a60fe3e06"  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    if keyword and keyword.capitalize() in countries:
        country_code = countries[keyword.capitalize()]
        url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}"
        print(f'Fetching news for {keyword}')
        speak(f'Fetching news for {keyword}')
    elif keyword:
        url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
        print(f"Fetching news with the keyword {keyword}")
        speak(f"Fetching news with the keyword {keyword}")
    try:
        response = requests.get(url).json()
        if response.get("articles"):
            print("Here are the top headlines:")
            speak("Here are the top headlines.")
            for article in response["articles"][:3]:
                title = article["title"]
                print(title)
                speak(title)
        else:
            speak("I couldn't fetch the news. Please check the keyword or country name.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak(f"An error occurred: {e}")

def set_reminder(reminder_time, message):
    try:
        if len(reminder_time) == 4 and reminder_time.isdigit():
            reminder_time = f"{reminder_time[:2]}:{reminder_time[2:]}"
        elif " " in reminder_time:
            parts = reminder_time.split()
            if len(parts) == 2 and all(part.isdigit() for part in parts):
                reminder_time = f"{parts[0]}:{parts[1]}"

        reminder_time = datetime.strptime(reminder_time, "%H:%M")
        print(f"Reminder set for {reminder_time.strftime('%I:%M %p')}")
        speak(f"Reminder set for {reminder_time.strftime('%I:%M %p')}")

        while True:
            now = datetime.now()
            if now.hour == reminder_time.hour and now.minute == reminder_time.minute:
                speak(f"Reminder: {message}")
                play_sound('alert.wav')
                break
            t.sleep(1)
    except ValueError:
        speak("The time format is invalid. Please say the time in HH MM or HH:MM format.")

def current_time():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    print(f"The current time is {time}.")
    speak(f"The current time is {time}.")

def current_date():
    now = datetime.now()
    date = now.strftime("%B %d, %Y")
    print(f"The current date is {date}.")
    speak(f"The current date is {date}.")

def main():
    speak("Hello! I am your assistant. How can I help you?")
    while True:
        command = listen()

        if "weather" in command:
            speak("Which city?")
            city = listen()
            get_weather(city)

        elif "news" in command:
            speak("Do you want to mention any specific country or a keyword?")
            keyword = listen()
            get_news(keyword if keyword else None)

        elif "reminder" in command:
            speak("At what time? Say in HH:MM format.")
            time = listen()
            speak("What should I remind you about?")
            message = listen()
            set_reminder(time, message)

        elif "time" in command:
            current_time()
            
        elif "date" in command:
            current_date()

        elif "stop" in command or "exit" in command:
            speak("Goodbye! Have a nice day.")
            play_sound('end.wav')
            break

        else:
            play_sound('fail.wav')
            speak("Sorry, can you say that again?")

if __name__ == '__main__':
    main()
