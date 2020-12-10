# Replaces one or many matches with a string
# Replace every white-space character with the number 9:
import re

#Replace all white-space characters with the digit "9":

txt = "Photography is my passion"
x = re.sub("\s", "9", txt)
print(x)


# You can control the number of replacements by specifying the count parameter:

# Replace the first 2 occurrences:

import re

txt = "Photography is my passion"
x = re.sub("\s", "9", txt, 2)
print(x)
