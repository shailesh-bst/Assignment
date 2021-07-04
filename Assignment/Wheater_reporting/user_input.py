import json


def get_user_input():
    try:
        user_input_file = open('weather.json', 'r')
        loc = user_input_file.read()
        user_input_obj = json.loads(loc)
        location = user_input_obj['City']
        variance = user_input_obj['Variance']
        location_list = []

        for i in range(len(location)):
            location_list.append(location[i])

        return location_list, variance

    except Exception as e:
        print(e)

