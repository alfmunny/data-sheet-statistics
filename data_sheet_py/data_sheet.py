# Data statistics generator written in python
import sys
import json
import os
import collections
from lib.printer import Printer 
from lib.statistic import Statistic
from lib.writer import Writer

# Test root
# SRC_DIR = '/Users/alfmunny/lernstift.data/WacomRecordings'
def main(argv=sys.argv):
    SRC_DIR = sys.argv[1]
    WACOM_DIR = SRC_DIR + '/WacomRecordings'
    TABLET_DIR = SRC_DIR + '/TabletRecordings/O2Collection/'
    PRES_DIR= SRC_DIR + '/Pressure'
    
    # Data sheet's destination
    W_STAT = 'writer_statistics.md'
    CSV_W = 'writer_wacom.csv'
    CSV_P = 'writer_pressure.csv'
    CSV_T = 'writer_tablet.csv'
    JS_W = 'wacom.js'
    JS_P = 'pressure.js'
    JS_T = 'tablet.js'
    
    s_wacom = Statistic(WACOM_DIR)
    s_tablet = Statistic(TABLET_DIR)
    s_pressure = Statistic(PRES_DIR)
    
    p_wacom = Printer(s_wacom)
    p_pressure = Printer(s_pressure)
    p_tablet = Printer(s_tablet)
   
    w_wacom = Writer('Yuanchen', WACOM_DIR)
    print("! Generating the data sheet, please do not interrupt !")

    p_wacom.print_csv_to(CSV_W)
    p_pressure.print_csv_to(CSV_P)
    p_tablet.print_csv_to(CSV_T) 
    
    p_wacom.print_js_to(JS_W)
    p_pressure.print_js_to(JS_P)
    p_tablet.print_js_to(JS_T) 
    
    print("√ Complete! The data sheets were created √")
if __name__ == "__main__":
    main(sys.argv)
