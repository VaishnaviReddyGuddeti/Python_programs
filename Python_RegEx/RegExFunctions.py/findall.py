# Returns a list containing all matches
# Print a list of all matches:
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



# If no matches are found, an empty list is returned:
# Return an empty list if no match was found:
import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
