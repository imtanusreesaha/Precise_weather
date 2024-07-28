{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNdAYFw1mrUyXkSi480UR8A",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/imtanusreesaha/Precise_weather/blob/main/weather%20forecast%20code.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fWkGgBnUtS0c",
        "outputId": "38b1120d-778e-4060-9fdd-71eed5e4d3eb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a city name: ranchi\n",
            "Current weather for ranchi:\n",
            "Temperature: 26.06°C\n",
            "Humidity: 94%\n",
            "Pressure: 998 hPa\n"
          ]
        }
      ],
      "source": [
        "import requests\n",
        "import json\n",
        "\n",
        "def get_weather_forecast(city):\n",
        "    api_key = \"d8957090639963e556861ce83d35b1b0\"\n",
        "    url = f\"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}\"\n",
        "    try:\n",
        "        response = requests.get(url)\n",
        "        response.raise_for_status()  # Raise an exception for HTTP errors\n",
        "        data = response.json()\n",
        "        return data\n",
        "    except requests.exceptions.HTTPError as http_err:\n",
        "        print(f\"HTTP error occurred: {http_err}\")\n",
        "    except requests.exceptions.RequestException as err:\n",
        "        print(f\"Other error occurred: {err}\")\n",
        "    except Exception as e:\n",
        "        print(f\"An unexpected error occurred: {e}\")\n",
        "    return None\n",
        "\n",
        "def main():\n",
        "    city = input(\"Enter a city name: \")\n",
        "    weather_data = get_weather_forecast(city)\n",
        "    if weather_data:\n",
        "        temperature_kelvin = weather_data[\"main\"][\"temp\"]\n",
        "        temperature_celsius = temperature_kelvin - 273.15  # Convert to Celsius\n",
        "        print(f\"Current weather for {city}:\")\n",
        "        print(f\"Temperature: {temperature_celsius:.2f}°C\")\n",
        "        print(f\"Humidity: {weather_data['main']['humidity']}%\")\n",
        "        print(f\"Pressure: {weather_data['main']['pressure']} hPa\")\n",
        "    else:\n",
        "        print(f\"Could not find weather data for {city}.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}