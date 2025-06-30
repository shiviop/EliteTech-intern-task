import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set your OpenWeatherMap API key here
API_KEY = '7b7ae5ad8be4db053751f3f9e9d13301' # Replace with your OpenWeatherMap API key

# City for which weather data will be fetched
CITY = input("enter city name")
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Send a GET request to OpenWeatherMap API
response = requests.get(URL)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch data:", response.json())
    exit()

# Parse JSON data
data = response.json()

# Extract relevant fields from the API response
timestamps = []
temperatures = []
humidities = []
pressures = []

for forecast in data['list']:
    dt = datetime.fromtimestamp(forecast['dt'])  # Convert UNIX timestamp to datetime
    temp = forecast['main']['temp']
    humidity = forecast['main']['humidity']
    pressure = forecast['main']['pressure']

    timestamps.append(dt)
    temperatures.append(temp)
    humidities.append(humidity)
    pressures.append(pressure)

# Set Seaborn theme
sns.set_theme(style="darkgrid")

# --- Create Visualization Dashboard ---

plt.figure(figsize=(15, 10))

# Temperature Plot
plt.subplot(3, 1, 1)
sns.lineplot(x=timestamps, y=temperatures, marker='o', color='red')
plt.title(f"Temperature Forecast for {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Humidity Plot
plt.subplot(3, 1, 2)
sns.lineplot(x=timestamps, y=humidities, marker='o', color='blue')
plt.title(f"Humidity Forecast for {CITY}")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

# Pressure Plot
plt.subplot(3, 1, 3)
sns.lineplot(x=timestamps, y=pressures, marker='o', color='green')
plt.title(f"Pressure Forecast for {CITY}")
plt.ylabel("Pressure (hPa)")
plt.xlabel("Date-Time")
plt.xticks(rotation=45)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the final dashboard
plt.show()
