# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "Abhishek",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Arush","Arshita"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Maserati", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
