# maketrans() - Returns a translation table to be used in translations

# translation table using a dictionary with maketrans()
# example dictionary
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict))
