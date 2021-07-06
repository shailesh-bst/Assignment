import user_input
import rest_api_weather
import numpy as np
import website
import config


# Task 1
def compare_temperatures(temp_website, temp_api):
    config.logger.info("Inside comparator")
    try:
        compared_values = abs(temp_website - temp_api)
        print("The temperature difference between every city respectively is: ")
        print(compared_values.tolist())
    except Exception as e:
        print(e)


# Task 2
def assert_temperature_variance(temp_website, temp_api, variance, city_list):
    try:
        config.logger.info("Inside variance assertion")
        for i in range(0, len(temp_api)):
            config.logger.info("Inside assertion loop")
            if abs(temp_website[i] - temp_api[i]) <= variance:
                print(str(city_list[i]) + " variance is OK")
            else:
                print(str(city_list[i]) + " variance mismatch. Stopping variance assertion")
                raise Exception
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        # getting values from user input file
        input_user = user_input.get_user_input()
        if input_user is not None:
            user_city_list = input_user[0]
            user_variance_input = input_user[1]

            # Fetching values from respective sources
            temperatures_of_cities_website = np.array(website.get_temp_site1(user_city_list))
            temperatures_of_cities_API = np.array(rest_api_weather.get_temp_site2(user_city_list))

            # Checking if any of the sources return None
            if temperatures_of_cities_website.any() and temperatures_of_cities_API.any() is not None:
                # Comparing two source temperatures
                compare_temperatures(temperatures_of_cities_website, temperatures_of_cities_API)

                # Checking variance
                assert_temperature_variance(temperatures_of_cities_website, temperatures_of_cities_API,
                                            user_variance_input, user_city_list)

            else:
                print("Either or both sources returned None")

        else:
            print("User values were not received")

    except Exception as e:
        print(e)



