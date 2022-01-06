"""
import my_module
courses = ['History', 'Math', 'Phusics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)

import my_module as mm
index = mm.find_index(courses, 'Math')
print(index)

from my_module import find_index
index = find_index(courses, 'Math')
print(index)

from my_module import find_index, test
index = find_index(courses, 'Math')
print(index)
print(test)

from my_module import find_index as fi, test
index = fi(courses, 'Math')
print(index)

from my_module import *
index = find_index(courses, 'Math')
print(index)
print(test)

from my_module import find_index, test
import sys

print(sys.path)
"""

"""
import sys
sys.path.append('/home/neila/Documents/my_module/')
print(sys.path)
	
from my_module import find_index, test

courses = ['History', 'Math', 'Phusics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
"""

"""
import random

courses = ['History', 'Math', 'Phusics', 'CompSci']

random_course = random.choise(courses)

print(random_course)
"""

import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))


import datetime
import calendar
today = datetime.date.today()
print(today)

print(calendar.isleap(2017))
print(calendar.isleap(2020))

import os
print(os.getcwd())
print(os.__file__)

import antigravity
