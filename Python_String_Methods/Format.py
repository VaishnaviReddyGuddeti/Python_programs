# format() - Formats specified values in a string
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# Using different placeholder values:
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "Sushanth", age = 26)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Sushanth",26)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Sushanth",26)

print(txt1)
print(txt2)
print(txt3)
