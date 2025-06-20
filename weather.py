from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Cairo"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather ***\n')

    city = input('\nEnter the city name: ')

    #chech for empty string or string with only spaces
    if not bool(city.strip()):
        city = "Cairo"


    weather = get_current_weather(city)

    print('\n')
    pprint(weather)