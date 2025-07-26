import requests

API_KEY = "2a4271be772c2065a4b19b118efc906d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            print(f"\n📍 Weather in {city.title()}:\n")
            print(f"🌤 Description: {weather}")
            print(f"🌡 Temperature: {temp}°C")
            print(f"💧 Humidity: {humidity}%\n")
        else:
            print("⚠️ City not found. Please try again.")
    except Exception as e:
        print("❌ Error fetching weather data:", e)

def main():
    print("== 🌦 Simple Weather CLI App ==")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("👋 Exiting Weather App. Stay safe!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
