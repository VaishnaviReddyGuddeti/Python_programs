# Use the separators parameter to change the default separator:
import json

x = {
  "name": "Vardhan",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Sara","Suraj"),
  "pets": None,
  "cars": [
    {"model": "Maserati", "mpg": 27.5},
    {"model": "MG Hector", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
