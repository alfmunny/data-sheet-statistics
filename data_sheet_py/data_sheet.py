# A data statistics generator written in python
import sys
import json
import os
import collections
from lib.printer import Printer 
from lib.statistic import Statistic
from lib.writer import Writer

# Test root
# SRC_DIR = '/Users/alfmunny/lernstift.data/WacomRecordings'

SRC_DIR = sys.argv[1]
WACOM_DIR = SRC_DIR + '/WacomRecordings'
TABLET_DIR = SRC_DIR + '/TabletRecordings/O2Collection'
PRES_DIR= SRC_DIR + '/Pressure'

# Data sheet's destination
W_STAT = 'writer_statistics.md'
CSV_W = 'writer_wacom.csv'
CSV_P = 'writer_pressure.csv'
CSV_T = 'writer_tablet.csv'

s_wacom = Statistic(WACOM_DIR)
s_tablet = Statistic(TABLET_DIR)
s_pressure = Statistic(PRES_DIR)

p_wacom = Printer(s_wacom)
p_pressure = Printer(s_pressure)
p_tablet = Printer(s_tablet)

print("! Generating the data sheet, please do not interrupt !")
p_wacom.print_csv_to(CSV_W)
p_pressure.print_csv_to(CSV_P)
p_tablet.print_csv_to(CSV_T)
#print("√ Complete! The data sheet " + W_STAT + " was created √")
