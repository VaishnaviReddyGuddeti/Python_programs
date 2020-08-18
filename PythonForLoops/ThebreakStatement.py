# With the break statement we can stop the loop before it has looped through all the items:

# Exit the loop when x is "BMW":

cars = ["Maserati", "BMW", "MG Hector"]
for x in cars:
  print(x)
  if x == "BMW":
    break
# Exit the loop when x is "BMW", but this time the break comes before the print:

cars = ["Maserati", "BMW", "MG Hector"]
for x in cars:
  if x == "BMW":
    break
  print(x)
