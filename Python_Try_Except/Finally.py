# The finally block, if specified, will be executed regardless if the try block raises an error or not

# #The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Try to open and write to a file that is not writable:

#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

#The program can continue, without leaving the file object open
