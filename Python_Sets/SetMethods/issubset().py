# 	Returns whether another set contains this set or not
# Return True if all items set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# What if not all items are present in the specified set?
# Return False if not all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)
