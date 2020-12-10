# *	Zero or more occurrences	"aix*"
import re

txt = "I am a foodie"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# *	Zero or more occurrences	"aix*"

import re

txt = "It is raining in hyderabad"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
