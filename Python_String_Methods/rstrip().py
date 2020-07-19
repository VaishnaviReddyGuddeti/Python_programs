# rstrip() - Returns a right trim version of the string

# Remove spaces to the right of the string:

txt = "     strawberry     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

# Remove the trailing characters:

txt = "strawberry,,,,,ssaaww....."

x = txt.rstrip(",.asw")

print(x)
