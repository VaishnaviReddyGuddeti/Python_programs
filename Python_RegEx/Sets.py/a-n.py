 #Returns a match for any lower case character, alphabetically between a and n

import re

txt = "Reading books is my habit"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
