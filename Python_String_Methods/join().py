# join() - Joins the elements of an iterable to the end of the string

# Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("Janu", "Parth", "Vikram")

x = "#".join(myTuple)

print(x)

# Join all items in a dictionary into a string, using a the word "TEST" as separator:

myDict = {"name": "Sushanth", "country": "India"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
