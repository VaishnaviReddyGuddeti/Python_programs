# \	Signals a special sequence (can also be used to escape special characters)
import re

txt = "That will be 59 rupees"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)
