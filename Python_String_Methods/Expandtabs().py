# expandtabs() - Sets the tab size of the string

# Set the tab size to 2 whitespaces:
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

# See the result using different tab sizes:
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
