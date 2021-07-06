import requests
import config


base_url = "http://api.openweathermap.org/data/2.5/weather?q="
api_key = "19e013c63cb9d49b16be2a2dba0dd61b"


def get_temp_site2(location_list):
    ''' TO get the temperature from openweathermap API '''
    temperature_list = []
    for i in range(0, len(location_list)):
        try:
            response = requests.request("GET", base_url + location_list[i] + "&appid=" + api_key)
            if response.status_code == 200:
                if response.content is not None:
                    kelvin_temp = response.json()["main"]["temp"]
                    celsius_temp = kelvin_temp - 273.15
                    temperature_list.append(int(celsius_temp))
            else:
                config.logger.info("The request was not processed for city")

        except Exception as e:
            print(e)

    if len(temperature_list) > 0:
        config.logger.info(" API Temperature list is not empty")
        return temperature_list
    else:
        config.logger.info("API Temperature list is empty")
        return None




