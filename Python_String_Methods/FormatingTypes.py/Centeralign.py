# :^	Center aligns the result (within the available space)

# #To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))

# := Places the sign to the left most position
# :+	Use a plus sign to indicate if the result is positive or negative
# :-	Use a minus sign for negative values only
# : 	Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
# :,	Use a comma as a thousand separator
# :_	Use a underscore as a thousand separator
# :b	Binary format
# :c	Converts the value into the corresponding unicode character
# :d	Decimal format
# :e	Scientific format, with a lower case e
# :E	Scientific format, with an upper case E
# :f	Fix point number format
# :F	Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g	General format
# :G	General format (using a upper case E for scientific notations)
# :o	Octal format
# :x	Hex format, lower case
# :X	Hex format, upper case
# :n	Number format
# :%	Percentage format
