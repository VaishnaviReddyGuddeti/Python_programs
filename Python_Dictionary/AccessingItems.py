# You can access the items of a dictionary by referring to its key name, inside square brackets
# Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:
# Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
