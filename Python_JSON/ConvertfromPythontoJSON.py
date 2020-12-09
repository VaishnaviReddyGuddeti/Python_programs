# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "Arjun",
  "age": 25,
  "city": "Bangalore"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
