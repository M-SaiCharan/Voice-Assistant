import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("There was a problem with the speech recognition service.")
        return ""


def get_weather(city):
    api_key = ""  # Replace with your weatherapi key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "current" in data:
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            print(f"The weather in {city} is {condition} with a temperature of {temp}°C.")
            speak(f"The weather in {city} is {condition} with a temperature of {temp}°C.")
        else:
            print("Error fetching weather data. Please check your API key or city name.")
            speak("Error fetching weather data. Please check your API key or city name.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak(f"An error occurred: {e}")


def get_news():
    api_key = "" # Replace your newsapi key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()

    if response.get("articles"):
        print("Here are the top headlines:")
        speak("Here are the top headlines:")
        for article in response["articles"][:3]:
            print(article["title"])
            speak(article["title"])
    else:
        speak("I couldn't fetch the news. Please check your API key.")


def set_reminder(reminder_time, message):
    reminder_time = datetime.strptime(reminder_time, "%H:%M")
    print(f"Reminder set for {reminder_time.strftime('%I:%M %p')}")
    speak(f"Reminder set for {reminder_time.strftime('%I:%M %p')}")
    while True:
        now = datetime.now()
        if now.hour == reminder_time.hour and now.minute == reminder_time.minute:
            speak(f"Reminder: {message}")
            break


def main():
    speak("Hello! I am your assistant. How can I help you?")
    while True:
        command = listen()

        if "weather" in command:
            speak("Which city?")
            city = listen()
            get_weather(city)

        elif "news" in command:
            get_news()

        elif "reminder" in command:
            speak("At what time? Say in HH:MM format.")
            time = listen()
            speak("What should I remind you about?")
            message = listen()
            set_reminder(time, message)

        elif "stop" in command or "exit" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I didn't understand that. Can you try again?")


if __name__ == '__main__':
    main()
