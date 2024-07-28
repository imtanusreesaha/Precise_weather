import requests
import json

def get_weather_forecast(city):
    api_key = "d8957090639963e556861ce83d35b1b0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def main():
    city = input("Enter a city name: ")
    weather_data = get_weather_forecast(city)
    if weather_data:
        temperature_kelvin = weather_data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15  # Convert to Celsius
        print(f"Current weather for {city}:")
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Pressure: {weather_data['main']['pressure']} hPa")
    else:
        print(f"Could not find weather data for {city}.")

if __name__ == "__main__":
    main()
