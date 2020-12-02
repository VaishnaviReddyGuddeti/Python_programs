# Set the age of p1 to 25:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("Shivam", 25)
p1.age = 25
print(p1.age)
