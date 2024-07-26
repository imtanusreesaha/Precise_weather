import requests
import json

def get_weather_forecast(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}".format(
        city=city,
        api_key="d8957090639963e556861ce83d35b1b0"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    else:
        return None

def main():
    city = input("Enter a city name: ")
    weather_data = get_weather_forecast(city)
    if weather_data:
        print("Current weather for {}:".format(city))
        print("Temperature: {}°C".format(weather_data["main"]["temp"]))
        print("Humidity: {}%".format(weather_data["main"]["humidity"]))
        print("Pressure: {}hPa".format(weather_data["main"]["pressure"]))
    else:
        print("Could not find weather data for {}.".format(city))

if __name__ == "__main__":
    main()