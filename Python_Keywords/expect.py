# If the statement raises an error print "Something went wrong":
# (x > 3) will raise an error because x is not defined:

# (x > 3) will raise an error because x is not defined:

try:
  x > 3
except:
  print("Something went wrong")
print("Even if it raised an error, the program keeps running")

# Write one message if it is a NameError, and another if it is an TypeError:
# (x > 3) will raise an error because x is a string and 3 is a number, and cannot be compared using a '>':

x = "hello"

try:
  x > 3
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
# Write a message if no errors were raised:
# (x > 10) will not raise any errors:

x = 1

try:
  x > 10
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
else:
  print("The 'Try' code was executed without raising any errors!")
