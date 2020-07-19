# index().py - Searches the string for a specified value and returns the position of where it was found
# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."

x = txt.index("e")

print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))
