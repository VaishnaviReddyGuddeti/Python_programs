# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 99
myfunc()
print(x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 30
def myfunc():
  global x
  x = 60
myfunc()
print(x)
