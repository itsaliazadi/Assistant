import requests
import datetime
import spacy
import re

def describeWeather(text):

    try:
        city = extractCity(text)  

        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_token = "fa84ec4967c9f7db6440f511825cbef4"

        url = base_url + "appid=" + api_token + "&q=" + city

        response = requests.get(url).json()

        weather_description = response["weather"][0]["description"]

        return weather_description
    except:
        return "Couldn't find the city"
    

def getTemperature(text):

    city = extractCity(text)

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_token = "fa84ec4967c9f7db6440f511825cbef4"

    url = base_url + "appid=" + api_token + "&q=" + city

    response = requests.get(url).json()

    temperature = response["main"]["temp"] - 273.15

    return temperature



    




def extractCity(text):

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    cities = [entity.text for entity in doc.ents if entity.label_ == "GPE"]

    if not cities:
        
        cities = re.findall(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*(?:, [A-Z]{2})?\b', text)

    try:
        return cities[0]
    except:
        return "-"


