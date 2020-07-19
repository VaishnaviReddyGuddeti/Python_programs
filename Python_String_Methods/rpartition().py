# rpartition() - Returns a tuple where the string is parted into three parts

# Search for the last occurrence of the word "bananas", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat strawberrys all day, strawberrys are my favorite fruit"

x = txt.rpartition("strawberry")

print(x)

txt = "I could eat strawberrys all day, strawberry are my favorite fruit"

x = txt.rpartition("strawberrys")

print(x)

# If the specified value is not found, the rpartition() method returns a tuple containing: 1 - an empty string, 2 - an empty string, 3 - the whole string:

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)
