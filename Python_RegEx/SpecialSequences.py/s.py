# Returns a match where the string contains a white space character	"\s"
import re

txt = "I like learning new things"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
