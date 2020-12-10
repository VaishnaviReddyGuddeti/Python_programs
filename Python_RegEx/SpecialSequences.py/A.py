# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
import re

txt = "The car is in black colour"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
