# Challenge 3
#### Assumptions:
- user has installed and configured machine to run python scripts.
- The JSON input will be valid.
- User enters only a single input.
#### Language and Modules used:
- Python to script the logic.
- The following modules are used in the script:
    - json: to read the json file.
    - requests: to make a http request to openweathermap api to fetch weather forcast details
#### Inputs:
- The script is designed to take three inputs, only one value is expected each time the script is run.
    1. URL mode - Press 1 to run the script to fetch the json object directly from the website using requests module.
    2. File mode -  Press 2 to run the script to fetch the json object from the test.json file included with the script.
    3. String mode - Press 3 to load a hardcoded json strng in the script and this would be used as the json object.
#### Algorithm:
    - read the input
    - find the value object of the key
        1. recursively read the object until a match is found.
        2. if match found return object[key].
        3. if no match, return None.
    - parse the value object to values
        1. parse the values recursively traversing theough a list/dict
        2. if single value, return the list else parse the list/dict to find individual values.
        3. return the values list.
    - print the values

#### Results : 
- To display the value of a key in a valid json.


