# Returns a set, that is the intersection of two other sets

# Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "tcs"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"apple", "banana", "cherry"}
z = x.intersection(y)
print(z)

#Compare 3 sets, and return a set with items that is present in all 3 sets:

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
