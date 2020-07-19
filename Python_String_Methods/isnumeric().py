# isnumeric() - Returns True if all characters in the string are numeric
# Check if all the characters in the text are numeric:

txt = "565543"

x = txt.isnumeric()

print(x)

# Check if the characters are numeric:
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
