# replace() - Returns a string where a specified value is replaced with a specified value

# Replace the word "bananas":

txt = "I like toys"

x = txt.replace("boll", "cars")

print(x)

# Replace all occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

# Replace the two first occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)
