# weather-app
# lib.py
# Classes and functions for weather-app.

# Function definitions.
# ---------------------

# Prompt for user input. Accepts a prompt message we want to show.
def prompt(msg):
    return input(msg)

def print_data(data_in):
    print("Date: {}".format(data_in['dt']))
    print("Description: {}".format(data_in['weather'][0]['description']))
    print("Temp: {}".format(data_in["main"]["temp"]))
    print("Wind: {} MPH".format(data_in["wind"]["speed"]))
    print("Pressure: {}".format(data_in['main']['pressure']))

# Class definitions.
# ------------------
class Payload:
    def __init__(self, city, country, user_key):
        self.city = city
        self.country = country
        self.user_key = user_key
        self.req = {
            "appid": self.user_key,
            "q": "{},{}".format(self.city, self.country),
            "units": "imperial"
        }
