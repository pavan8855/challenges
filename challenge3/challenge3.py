#challenge3.py

import json
import requests

## The module returns the value of a key in the json.
# pass the json object and key to retrieve the matching object.
def json_match(obj, key):
    global final_json
    if type(obj) is dict and obj:
        for obj_key in obj:
            if key == obj_key:
                final_json = obj[obj_key]
                return 0
            else:
                json_match(obj[obj_key], key)
    elif type(obj) is list and obj:
        for item in obj:
            json_match(item, key)
    return 0

#the module parses the matched object to retrieve the values within the object.
#pass in the object retrieved from the json_match to get the list of values associated with the key.
def parse_json(obj):
    global result
    if type(obj) is dict and obj:
        for obj_key in obj:
            if type(obj[obj_key]) is dict and obj[obj_key]:
                parse_json(obj[obj_key])
            elif type(obj[obj_key]) is list and obj[obj_key]:
                for item in obj[obj_key]:
                    parse_json(item)
            else:
                result.append(obj[obj_key])
    elif type(obj) is list and obj:
        for item in obj:
            parse_json(item)
    else:
        result.append(obj)
    return 0

# the script provides three input choices
# 1. URL - fetches the json from open weather map website and parses the weather data
# 2. File - loads the json from test.json and parses the weather data - source openweathermap
# 3. String - the string is hardcoded below.
# the output returns the values of the matching key, if no match - key not found message is displayed.
result = []
final_json = None
inp = int(input("Enter your choice of input (1 for URL, 2 for file, 3 for string)"))

if inp == 1:
    api_key = "267116c31744c89aefd40fc4dc6c5dd6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Bangalore"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    obj = response.json()
    if obj["cod"] != "404":
        key = "weather"

elif inp == 2:
    file = open("test.json")
    obj = json.load(file)
    file.close()
    key = "coord"

elif inp == 3:
    obj = {"a":[{"b":{"c":[{"d": 456},{"ef": "man"}]}},{"x":{"y":[{"z": 123},{"ab": "val"}]}}]}
    key = "a"
else:
    print("not a valid input")

json_match(obj, key)

parse_json(final_json)

if result != None:
    print(result)
else:
    print("key not found")

exit(0)


