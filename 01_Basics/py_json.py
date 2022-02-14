# JSON is commonly used with data APIS. Here's how we can parse JSON into a Python dictionary

import json

# sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "Age": 30}'

# parse to dict

user = json.loads(userJSON)

# Prits dictionary
print(user)

print(user['first_name'])

# Turn a dict into JSON format

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(f'The json for car is {carJSON}')