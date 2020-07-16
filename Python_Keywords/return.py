# To exit a function and return a value
# Exit a function and return the sum:
def myfunction():
  return 3+3
print(myfunction())
# Statements after the return line will not be executed:
def myfunction():
  return 3+3
print("Hello, World!")
print(myfunction())
