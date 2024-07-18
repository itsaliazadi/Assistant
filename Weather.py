import requests
import datetime

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_token = "fa84ec4967c9f7db6440f511825cbef4"
city = "Yakutsk"

url = base_url + "appid=" + api_token + "&q=" + city

response = requests.get(url).json()

weather_description = response["weather"][0]["description"]
temperature = response["main"]["temp"] - 273.15

print(weather_description)
print(temperature)
