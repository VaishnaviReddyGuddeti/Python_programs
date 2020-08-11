# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
# Join two list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# Another way to join two lists are by appending all the items from list2 into list1, one by one:
#Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
