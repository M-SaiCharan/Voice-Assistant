
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
1. **Python**:
   - Ensure you have Python 3.7 or above installed on your system.

2. **API Keys**:
   - **WeatherAPI**: Sign up at [WeatherAPI](https://www.weatherapi.com/) to obtain an API key.
   - **NewsAPI**: Sign up at [NewsAPI](https://newsapi.org/) to obtain an API key.
  
## Setup Instructions
1. Clone this repository to your local system using Git:

   ```bash
   git clone https://github.com/M-SaiCharan/Voice-Assistant.git
   ```

2. Install Dependencies:
   Use the following command to install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run
1. Replace the placeholders for API keys in the `get_weather` and `get_news` functions in main.py with your actual keys.
2. Run the script using Python:
   
   ```bash
   python main.py
   ```
   
3. The assistant will start listening for your commands.

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
- User: "How is the weather?"
- Assistant: "Which city?"
- User: "New York"
- Assistant: "The weather in New York is partly cloudy with a temperature of 20°C."

## Troubleshooting
1. Ensure your microphone is properly configured.
2. Check your internet connection for API calls.
3. Validate the API keys and replace them if expired.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as you include the original license in any copies or substantial portions of the software.

For more details, refer to the [LICENSE](LICENSE) file included in the project.

> Copyright &copy; 2024 M-SaiCharan

