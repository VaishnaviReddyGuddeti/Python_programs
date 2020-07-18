# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
 txt = "We are the so-called "Vikings" from the north."

#You will get an error if you use double quotes inside a string that are surrounded by double quotes:
# To fix this problem, use the escape character \":
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
