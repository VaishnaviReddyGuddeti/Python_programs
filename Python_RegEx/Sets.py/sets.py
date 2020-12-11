# In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

import re

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
