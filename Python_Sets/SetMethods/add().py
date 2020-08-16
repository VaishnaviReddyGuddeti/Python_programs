# Adds an element to the set
# If the element already exists, the add() method does not add the element
# Add an element to the fruits set:

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# Try to add an element that already exists:

fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)
