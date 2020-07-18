# Encode() - Returns an encoded version of the string
# Syntax - string.encode(encoding=encoding, errors=errors)

# UTF-8 encode the string:
txt = "My name is Sushanth"

x = txt.encode()

print(x)

# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print(txt.encode(encoding="ascii",errors="strict"))
