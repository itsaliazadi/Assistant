import requests
import spacy
import re
import os

def getWeatherData(text):
    city = extractCity(text)  

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_token = os.environ.get("OPENWEATHERMAP_API_TOKEN")

    url = base_url + "appid=" + api_token + "&q=" + city

    response = requests.get(url).json()

    return response


def describeWeather(text) -> str:

    try:
        response = getWeatherData(text)
        weather_description = response["weather"][0]["description"]
        return weather_description
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data"
    
    except IndexError:
        return "No city found in the text"
    
    except Exception as e:
        print(e)
        return f"An unexpected error occurred"
    

def getTemperature(text) -> float:
    try:
        response = getWeatherData(text)
        temperature = round(response["main"]["temp"] - 273.15, 2)
        return temperature
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data"
    
    except IndexError:
        return "No city found in the text"
    
    except Exception as e:
        return f"An unexpected error occurred"


def extractCity(text) -> str:

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    cities = [entity.text for entity in doc.ents if entity.label_ == "GPE"]

    if not cities:
        
        cities = re.findall(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*(?:, [A-Z]{2})?\b', text)

    try:
        return cities[0]
    except:
        return "-"


