# Returns whether this set contains another set or not
# Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# What if not all items are present in the specified set?

# Return False if not all items in set y are present in set x:

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
