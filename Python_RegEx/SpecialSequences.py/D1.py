# Returns a match where the string DOES NOT contain digits	"\D"
import re

txt = "I like traveling "

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
