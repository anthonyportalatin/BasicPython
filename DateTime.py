#This program introduces datetime module

from datetime import datetime

print (datetime.now())

now = datetime.now()
year = now.year
day = now.day
month = now.month
hour = now.hour
minute = now.minute
seconds = now.second

print ("Date: %s/%s/%s \nTime: %s:%s:%s" %(month, day, year, hour, minute, seconds))
