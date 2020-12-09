# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# Convert from JSON to Python:
import json

# some JSON:
x = '{ "name":"Shivam", "age":30, "city":"Bangalore"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
