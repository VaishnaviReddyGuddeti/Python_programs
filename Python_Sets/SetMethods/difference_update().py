# 	Removes the items in this set that are also included in another, specified set

# Remove the items that exist in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"apple", "banana", "cherry"}
x.difference_update(y)
print(x)
