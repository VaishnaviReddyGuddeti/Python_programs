# Returns a list of all the values in the dictionary

# Return the values:

car = {
  "brand": "BMW",
  "model": "X5",
  "year": 1999
}

x = car.values()

print(x)


# When a values is changed in the dictionary, the view object also gets updated:

car = {
  "brand": "BMW",
  "model": "X5",
  "year": 1986
}

x = car.values()

car["year"] = 2020

print(x)
