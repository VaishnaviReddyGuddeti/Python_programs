# 	Returns a match where the string DOES NOT contain any word characters	"\W"

import re

txt = "The rain in India"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
