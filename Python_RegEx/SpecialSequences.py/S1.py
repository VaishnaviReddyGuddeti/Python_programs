# Returns a match where the string DOES NOT contain a white space character	"\S"
import re

txt = " Life is full of ups and downs"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
