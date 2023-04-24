import random
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

rand = random.choice(courses)
print(rand)


today = datetime.date.today()
print(today)

print(calendar.isleap(2023))


print(os.getcwd())

# this will print out the location of this module file
print(os.__file__)
