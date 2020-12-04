# Week number of year, Monday as the first day of week, 00-53
import datetime

x = datetime.datetime(2018, 5, 31)

print(x.strftime("%W"))
