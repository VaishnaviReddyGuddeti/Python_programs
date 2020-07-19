# rjust() - Returns a right justified version of the string

# Return a 20 characters long, right justified version of the word "banana":

txt = "strawberry"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

# Using the letter "O" as the padding character:

txt = "strawberry"

x = txt.rjust(20, "O")

print(x)
