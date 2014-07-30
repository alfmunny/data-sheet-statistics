# A data statistics generator written in python
import sys
import json
import os
import collections
sys.path.append('./lib')
from printer import Printer 
from statistic import Statistic

# test root
#SRC_DIR = '/Users/alfmunny/lernstift.data/WacomRecordings'

SRC_DIR = sys.argv[1]
WACOM_DIR = SRC_DIR + '/WacomRecordings'
print(WACOM_DIR)

# data sheet's destination
W_STAT = 'writer_statistics.md'

s = Statistic(WACOM_DIR)
printer = Printer(s)

print("! Generating the data sheet, please do not interrupt !")
printer.print_to(W_STAT)
print("√ Complete! The data sheet " + W_STAT + " was created √")
