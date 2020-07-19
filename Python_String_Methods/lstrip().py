# lstrip() - Returns a left trim version of the string

# Remove spaces to the left of the string:

txt = "     apple     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

# Remove the leading characters:

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)
