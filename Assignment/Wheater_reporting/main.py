import user_input
import rest_api_weather
import numpy as np
import website


# Task 1
def compare_temperatures(temp_website, temp_api):
    compared_values = abs(temp_website - temp_api)
    print("The difference between every city temperature is: ")
    print(compared_values.tolist())


# Task 2
def assert_temperature_variance(temp_website, temp_api, variance):
    for i in range(0, len(temp_website)):
        assert abs(temp_website[i] - temp_api[i]) <= variance
        print(i + "In range")


if __name__ == "__main__":
    # getting values from user input file
    input_user = user_input.get_user_input()
    if input_user is not None:
        # Fetching values from respective sources
        temperatures_of_cities_website = np.array(website.get_temp_site1(input_user[0]))
        temperatures_of_cities_API = np.array(rest_api_weather.get_temp_site2(input_user[0]))
        # Comparing two source temperatures
        compare_temperatures(temperatures_of_cities_website, temperatures_of_cities_API)
        # Checking variance
        assert_temperature_variance(temperatures_of_cities_website, temperatures_of_cities_API, input_user[1])

    else:print("User values were not received")

