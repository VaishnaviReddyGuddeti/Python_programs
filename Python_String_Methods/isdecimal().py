# isdecimal() - Returns True if all characters in the string are decimals
# Check if all the characters in the unicode object are decimals:
txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)

# Check if all the characters in the unicode are decimals:
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())
