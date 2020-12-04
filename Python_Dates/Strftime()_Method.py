# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string
# Display the name of the month:
import datetime

x = datetime.datetime(2020, 12, 4)

print(x.strftime("%B"))
