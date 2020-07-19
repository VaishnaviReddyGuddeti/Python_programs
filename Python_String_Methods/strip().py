# strip() - Returns a trimmed version of the string

# Remove spaces at the beginning and at the end of the string:

txt = "    strawberry    "

x = txt.strip()

print("of all fruits", x, "is my favorite")

# Remove the leading and trailing characters:

txt = ",,,,,rrttgg.....strawberry....rrr"

x = txt.strip(",.grt")

print(x)
