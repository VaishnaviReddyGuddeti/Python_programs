# Week number of year, Sunday as the first day of week, 00-53
import datetime

x = datetime.datetime.now()

print(x.strftime("%U"))
