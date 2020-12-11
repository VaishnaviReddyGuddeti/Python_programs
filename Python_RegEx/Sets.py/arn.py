# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
import re

txt = "I love eating ice-cream"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
