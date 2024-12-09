
# Voice Assistant Project

This project implements a simple voice assistant in Python. The assistant can provide weather updates, read news headlines, and set reminders based on voice commands.

## Features
1. **Weather Updates**:
   - Get real-time weather information for a specified city using the WeatherAPI.

2. **News Headlines**:
   - Fetch and read out the top three news headlines from NewsAPI.

3. **Reminders**:
   - Set a reminder with a specific time and message.

4. **Voice Interaction**:
   - Uses speech recognition and text-to-speech to interact with the user.

## Prerequisites
1. **Python Libraries**:
   - `speech_recognition`: For speech-to-text.
   - `pyttsx3`: For text-to-speech.
   - `requests`: For making API calls.

   Install these dependencies using pip:
   ```bash
   pip install speechrecognition pyttsx3 requests
   ```

2. **API Keys**:
   - **WeatherAPI**: Sign up at [WeatherAPI](https://www.weatherapi.com/) to obtain an API key.
   - **NewsAPI**: Sign up at [NewsAPI](https://newsapi.org/) to obtain an API key.

## How to Run
1. Clone the project or copy the Python script.
2. Replace the placeholders for API keys in the `get_weather` and `get_news` functions with your actual keys.
3. Run the script using Python:
   ```bash
   python script_name.py
   ```
4. The assistant will start listening for your commands.

## Commands
1. **Weather**:
   - Say "weather" to fetch weather details.
   - The assistant will prompt you to specify a city.

2. **News**:
   - Say "news" to hear the top news headlines.

3. **Reminder**:
   - Say "reminder" to set a reminder.
   - Provide the time in HH:MM format and a message.

4. **Exit**:
   - Say "stop" or "exit" to close the assistant.

## Example Usage
- User: "What's the weather in New York?"
- Assistant: "The weather in New York is partly cloudy with a temperature of 20°C."

## Troubleshooting
1. Ensure your microphone is properly configured.
2. Check your internet connection for API calls.
3. Validate the API keys and replace them if expired.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as you include the original license in any copies or substantial portions of the software.

For more details, refer to the [LICENSE](LICENSE) file included in the project.

> Copyright &copy; 2024 M-SaiCharan

