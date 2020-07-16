# To make a try...except statement
# Try a block of code, and decide what to to if it raises an error:
# (x > 3) will raise an error because x is not defined:

try:
  x > 3
except:
  print("Something went wrong")
print("Even if it raised an error, the program keeps running")
# Raise an error and stop the program when there is an error in the try block:
try:
  x > 3
except:
  raise Exception("Something went wrong")
print("The program stops when an error is raised.")
