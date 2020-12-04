# Weekday as a number 0-6, 0 is Sunday
import datetime

x = datetime.datetime.now()

print(x.strftime("%w"))
