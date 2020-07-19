# rsplit() - Splits the string at the specified separator, and returns a list

# Split a string into a list, using comma, followed by a space (, ) as the separator:

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

# Split the string into a list with maximum 2 items:

txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)

# note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.
