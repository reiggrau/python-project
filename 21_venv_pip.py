# Create virtual environment
# py -m venv .venv

# To activate the venv
# source .venv/Scripts/activate

# To deactivate
# deactivate

# Install 'requests' in the venv
# py -m pip install requests

# Check installed packages
# py -m pip list

# Check details of package
# py -m pip show requests

# Install python-dotenv
# py -m pip install python-dotenv

# Python package index
# https://pypi.org/

# Create list of requirements
# py -m pip freeze > requirements.txt

##################
# https://openweathermap.org/

import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    print("\n*** Current Weather Conditions ***\n")

    city = input("Please enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)  # pretty print

    print(f"\nCurrent weather for: {weather_data['name']}")
    print(f"The sky is: {weather_data['weather'][0]['description']}")
    print(f"The temperature is: {weather_data['main']['temp']} °C")
    print(f"The humidity is: {weather_data['main']['humidity']} %")


if __name__ == "__main__":
    get_current_weather()
