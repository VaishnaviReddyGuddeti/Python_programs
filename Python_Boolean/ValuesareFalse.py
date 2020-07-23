#There are not many values that evaluates to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

# The following will return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
