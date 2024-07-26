# Precise Weather
# CODE-MAVERICK
Microsoft Hackathon
# Weather Forecasting Tool

The Weather Forecasting Tool is a command line tool that accepts a city's name as input and returns the current weather forecast. It leverages the OpenWeatherMap API to fetch weather data and parse it using Python.


# THE ARCHITECTURAL FLOW OF THE CODE IS:

Weather Forecast CLI Tool

This command line tool accepts a city name as input and returns the current weather forecast for that city. It leverages the OpenWeatherMap API to fetch weather data and parses it using Python.

# Architecture Flow:

1. User Input:
   - The tool prompts the user to enter a city name through the command line.

2. API Request:
   - The city name provided by the user is used to construct an API URL for the OpenWeatherMap API.
   - The tool makes an HTTP GET request to the API URL using the `requests` module.
   - If the API request is successful (HTTP status code 200), the response content is obtained.

3. Data Parsing:
   - The response content, in JSON format, is parsed using the `json` module's `loads()` function.
   - The parsed data is stored in a Python dictionary.

4. Data Display:
   - If the weather data dictionary is not empty, the tool displays the current weather information for the city.
   - The temperature, humidity, and pressure are extracted from the weather data dictionary and printed on the command line.
   - If the weather data dictionary is empty, a message is displayed indicating that weather data for the city could not be found.

Usage:

1. Install Dependencies:
   - Ensure that Python is installed on your system.
   - Install the `requests` module by running `pip install requests` in your terminal.

2. Obtain an API Key:
   - Sign up on the OpenWeatherMap website to obtain an API key.
   - Replace `"YOUR_API_KEY"` in the Python code with your actual API key.

3. Run the Tool:
   - Open a terminal and navigate to the directory where the Python script is located.
   - Run the script by executing the command `python weather_forecast.py`.
   - Enter the name of the city for which you want to retrieve the weather forecast.
   - The tool will display the current weather information if available.

Note: The tool uses the metric system for temperature (°C) and pressure (hPa).

