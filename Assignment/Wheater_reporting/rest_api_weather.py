import requests
import json


base_url = "http://api.openweathermap.org/data/2.5/weather?q="
api_key = "19e013c63cb9d49b16be2a2dba0dd61b"


def get_temp_site2(location_list):
    ''' TO get the temperature from openweathermap API '''
    temperature_list = []
    for i in range(0, len(location_list)):
        try:
            response = requests.request("GET", base_url + location_list[i] + "&appid=" + api_key)
            kelvin_temp = response.json()["main"]["temp"]
            celsius_temp = kelvin_temp - 273.15
            temperature_list.append(int(celsius_temp))
        except Exception as e:
            print(e)

    return temperature_list




