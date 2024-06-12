import requests

def mausam(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        country = data["sys"]["country"]

        print(f"Weather in {city}, {country}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found. Please enter a valid city name.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "9643d56c800a193006f7d2bc103540ad"  

    mausam(city, api_key)
