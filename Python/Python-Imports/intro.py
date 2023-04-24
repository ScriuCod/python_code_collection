import sys

import my_module
import my_module as mm
from my_module import find_index, test

# do not use this, will lower the readability of the code
# from my_module import find_index as fi, test


# if you use this you will not know what come from where
# from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
index2 = mm.find_index(courses, 'Math')
index3 = find_index(courses, 'Math')
print(index)
print(index2)
print(index3)

print(test)
print(sys.path)

