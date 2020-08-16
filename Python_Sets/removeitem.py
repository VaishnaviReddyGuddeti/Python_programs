# To remove an item in a set, use the remove(), or the discard() method.

# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Remove the last item by using the pop() method:
# returns the removed value by using pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
