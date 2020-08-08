# You can specify a range of indexes by specifying where to start and where to end the range
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

# This example returns the items from the beginning to "orange":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
# By leaving out the end value, the range will go on to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
