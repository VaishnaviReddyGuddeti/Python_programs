# Removes the last inserted key-value pair

# Remove the last item from the dictionary:

car = {
  "brand": "BMW",
  "model": "X5",
  "year": 2020
}

car.popitem()

print(car)

# The removed item is the return value of the pop() method:

car = {
  "brand": "BMW",
  "model": "X5",
  "year": 2020
}

x = car.popitem()

print(x)
