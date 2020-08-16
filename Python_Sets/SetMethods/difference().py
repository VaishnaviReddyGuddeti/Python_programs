# Returns a set containing the difference between two or more sets

# Return a set that contains the items that only exist in set x, and not in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"cherry", "apple", "banana"}
z = x.difference(y)
print(z)
