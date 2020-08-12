# Add the elements of a list (or any iterable), to the end of the current list
# add the elements of cars and colors

cars = ["Maserati Quattroporte" , "BMW" , "MG Hector"]
colors = ["Blue" , " Black ", "White"]
colors.extend(cars)
print(colors)

# Add a tuple to the bikes list:
bikes = ['BMW K 1300 R' , 'Royal Enfield' , 'Harley Davidson']
points = (1, 4, 5, 9)
bikes.extend(points)
print(bikes)
