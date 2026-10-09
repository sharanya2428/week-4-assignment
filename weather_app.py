import requests

API_KEY = "YOUR_API_KEY"
city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params, timeout=10)

if response.status_code == 200:
    data = response.json()
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Could not get weather. Check city and API key.")
