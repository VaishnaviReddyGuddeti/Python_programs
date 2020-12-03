# The function will print the local x, and then the code will print the global x:
x = 88
def myfunc():
  x = 99
  print(x)
myfunc()
print(x)
