# Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# The finally block will always be executed, no matter if the try block raises an error or not:
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")
