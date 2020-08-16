# Remove the specified item

# Remove "banana" from the set:

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# OR

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


fruits = {"apple", "banana", "cherry"}
fruits.discard("banana", "apple" ,"cherry")
print(fruits)
