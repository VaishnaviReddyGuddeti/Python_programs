# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

# Get the value of the "model" item:

car = {
  "brand": "BMW",
  "model": "X5",
  "year": 2020
}

x = car.setdefault("model", "Bronco")

print(x)

# Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":

car = {
  "brand": "BMW",
  "model": "X5",
  "year": 2020
}

x = car.setdefault("color", "black")

print(x)
