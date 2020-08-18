# inserts the symmetric differences from this set and another
# Remove the items that are present in both sets, AND insert the items that is not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
