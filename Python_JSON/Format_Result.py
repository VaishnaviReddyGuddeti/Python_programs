# The json.dumps() method has parameters to make it easier to read the result:
# Use the indent parameter to define the numbers of indents:
import json

x = {
  "name": "Anurag",
  "age": 29,
  "married": True,
  "divorced": False,
  "children": ("Arav","Arjun"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "MG Hector", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
