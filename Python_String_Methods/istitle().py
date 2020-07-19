# istitle() - Returns True if the string follows the rules of a title

#Check if each word start with an upper case letter:

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

# Check if each word start with an upper case letter:

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
