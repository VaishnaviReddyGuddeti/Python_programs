# 	Returns a match for any character EXCEPT a, r, and n
import re

txt = "I love eating ice-cream"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
