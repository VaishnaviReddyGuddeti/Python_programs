# endswitch() - Returns true if the string ends with the specified value
# Syntax - string.endswith(value, start, end)

# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

# Check if the string ends with the phrase "my world.":
txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)

# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)
