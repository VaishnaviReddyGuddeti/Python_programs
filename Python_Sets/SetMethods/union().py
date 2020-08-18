# Return a set containing the union of sets
# Return a set that contains all items from both sets, duplicates are excluded:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# Unify more than 2 sets:

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)
