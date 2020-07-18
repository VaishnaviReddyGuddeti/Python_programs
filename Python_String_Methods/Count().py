# Count() - Returns the number of times a specified value occurs in a string
# Syntax - string.count(value, start, end)
# Parameter Values:
# 1.value -	Required. A String. The string to value to search for
# 2.start -	Optional. An Integer. The position to start the search. Default is 0
# 3.end	- Optional. An Integer. The position to end the search. Default is the end of the string

# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)
