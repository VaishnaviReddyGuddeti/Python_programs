# isdigit() - Returns True if all characters in the string are digits
# Check if all the characters in the text are digits:
txt = "50800"

x = txt.isdigit()

print(x)

# Check if all the characters in the text is alphabetic:
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())
