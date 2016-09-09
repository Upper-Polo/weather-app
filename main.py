# weather-app
# main.py

from sys import argv, exit
import requests
import lib

def main():
    try:
        api_key = argv[1]
    except IndexError:
        print('Pass in AP key')
        exit(0)

    payload = {
        "appid": api_key,
        "q": "Lexington,us",
        "units": "imperial",
    }



    r = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)

    print(r.url)
    weather_data = r.json()

    lib.print_data(weather_data)

    

if __name__ == '__main__':
    main()