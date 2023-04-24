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

# this is very useful to search a file inside a tree
for dirpath, dirnames, filenames in os.walk("/Users/ihelerea/dev/Adri/repos/python_code_collection/Python/"):
    print(f'Directory Path: {dirpath}')
    print(f'Directories Name: {dirnames}')
    print(f'Files Name: {filenames}')
