# partition() - Returns a tuple where the string is parted into three parts

# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

# If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)
