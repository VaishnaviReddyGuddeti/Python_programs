#You can use the else keyword to define a block of code to be executed if no errors were raised:
#In this example, the try block does not generate any error:

#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
