# Returns a match if the specified characters are at the end of the string	"Spain\Z"

import re

txt = "Dream big and achieve by doing hard and smart work"

#Check if the string ends with "Work":

x = re.findall("work\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
