# Built by Team CODE MAVERICK 🚀 for the Microsoft Hackathon

# 🌦️ Precise Weather Forecasting Tool

A command-line application that fetches and displays current weather data for any city using the **OpenWeatherMap API**. Developed as part of **Microsoft Hackathon - CODE MAVERICK**, this tool demonstrates API integration, JSON parsing, and real-time data handling using Python.

## 🔧 Features

- 🌍 Fetches real-time weather data by city name  
- 🌡️ Displays temperature, humidity, and pressure  
- ⚙️ Uses **OpenWeatherMap API** for reliable forecasts  
- 🧰 Lightweight, fast, and easy to use from the command line  

## 🧭 Architecture Flow

```
User Input → API Request → JSON Parsing → Data Extraction → Weather Output
```

1. **User Input**: Prompt for city name via CLI  
2. **API Request**: Constructs API URL & sends HTTP GET request  
3. **Data Parsing**: Parses JSON response into Python dictionary  
4. **Display Output**: Shows temperature, humidity, and pressure  

---

## 💻 Usage

### 🔧 Prerequisites

- Python installed on your system  
- Install dependencies:  
```bash
pip install requests
```

- Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api)

### 🚀 Running the Tool

1. Replace `"YOUR_API_KEY"` in the script with your actual API key  
2. Open terminal and navigate to the script folder  
3. Run the tool:  
```bash
python weather.py
```
4. Enter a city name when prompted  
5. Get the current weather details instantly  

> 🌡️ *Note: Uses metric units – Temperature (°C), Pressure (hPa)*

---

## 🧰 Tech Stack

- Python  
- Requests (HTTP library)  
- JSON parsing  

---

## 📁 Project Structure

```
├── weather.py            # Main script
├── weather.jpg           # Optional: Weather banner
└── README.md             # Project documentation
```

---

## 📸 Sample Output

```
Enter city name: London
Temperature: 15°C
Humidity: 72%
Pressure: 1013 hPa
```
## 👥 Team
👩‍💻 Tanusree Saha

GitHub: @imtanusreesaha

👨‍💻 Aditya Akhouri

GitHub: @Adityaakhouri


---

## 📜 License

This project is open source under the [MIT License](LICENSE).

---

Let me know if you’d like help with a logo, badges (e.g., Python version, license), or adding GitHub Actions for CI!

