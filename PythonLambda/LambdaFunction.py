# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# Or, use the same function definition to make a function that always triples the number you send in:

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

# Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
