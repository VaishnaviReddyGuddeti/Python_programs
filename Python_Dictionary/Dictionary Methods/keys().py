# Returns a list containing the dictionary's keys
# Return the keys:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)


# When an item is added in the dictionary, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "Blue"

print(x)
