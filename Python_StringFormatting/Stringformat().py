# The format() method allows you to format selected parts of a string.
# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} rupees"
print(txt.format(price))

# Format the price to be displayed as a number with two decimals:
price = 49
txt = "The price is {:.2f} rupees"
print(txt.format(price))
