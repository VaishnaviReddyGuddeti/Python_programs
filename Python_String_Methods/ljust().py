# ljust() - Returns a left justified version of the string

# Return a 20 characters long, left justified version of the word "banana":

txt = "apple"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

# Using the letter "O" as the padding character:

txt = "apple"

x = txt.ljust(20, "O")

print(x)
