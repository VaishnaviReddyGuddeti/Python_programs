# To test if two variables are equal
# Check if two objects are the same object:
x = ["apple", "banana", "cherry"]
y = x
print(x is y)
# Test two objects that are equal, but not the same object:
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)
