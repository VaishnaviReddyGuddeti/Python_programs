# Removes the element with the specified key

# Remove "model" from the dictionary:

car = {
  "brand": "BMW",
  "model": "X1",
  "year": 2020
}

car.pop("model")

print(car)

# The value of the removed item is the return value of the pop() method:

car = {
  "brand": "BMW",
  "model": "X1",
  "year": 2020
}

x = car.pop("model")

print(x)
