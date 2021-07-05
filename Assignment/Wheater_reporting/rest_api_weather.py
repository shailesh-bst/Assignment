import json
import config


def get_user_input():
    try:
        user_input_file = open('weather.json', 'r')
        config.logger.info("User input file is present")

        loc = user_input_file.read()
        user_input_obj = json.loads(loc)

        location = user_input_obj['City']
        variance = user_input_obj['Variance']
        config.logger.info("The two require fields location and variance have been provided")

        # Final city  list to be returned
        location_list = []
        for i in range(len(location)):
            location_list.append(location[i])

        if len(location_list) > 0:
            config.logger.info("City list and variance values are fetched")
            return location_list, variance
        else:
            config.logger.info("For loop failed to append user inputted city values in final list")
            return None

    except Exception as e:
        print(e)

