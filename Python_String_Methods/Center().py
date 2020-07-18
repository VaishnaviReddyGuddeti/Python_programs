# Center() - Returns a centered string
# Syntax - string.center(length, character)
# Parameter Values :- Length : The length of the returned string And Character :The character to fill the missing space on each side. Default is " " (space)

# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"

x = txt.center(20)

print(x)

# Using the letter "O" as the padding character:
txt = "banana"

x = txt.center(20, "O")

print(x)
