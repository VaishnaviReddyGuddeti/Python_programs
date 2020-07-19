# split() - Splits the string at the specified separator, and returns a list

# Split a string into a list where each word is a list item:

txt = "welcome to the home"

x = txt.split()

print(x)

# Split the string, using comma, followed by a space, as a separator:

txt = "hello, my name is Sushanth, I am 26 years old"

x = txt.split(", ")

print(x)

# Use a hash character as a separator:

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

# Split the string into a list with max 2 items:

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)
