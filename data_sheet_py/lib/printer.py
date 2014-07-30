import sys
import os
from lib.writer import Writer

# A printer class to help printing out the data sheet to some defined destinations
class Printer:
    def __init__(self, statistic):
        self.statistic = statistic 
    
    def print_md_to(self, filepath):
        writers = self.statistic.get_writers()
        if os.path.isfile(filepath):
            os.remove(filepath)
        for writer in writers:
            w = Writer(writer, self.statistic.root)
            f = open(filepath, 'a')
            f.write(w.name)
            f.write('\n===\n\n')
            if 'Pressure' in self.statistic.root:
                letters = w.get_letters_pressure()
            else:
                letters = w.get_letters()
            to_sort = []
            for i in letters:
                to_sort.append(i)
            for letter in sorted(to_sort):
                f.write('\t' + letter + '\t' + str(letters[letter]))
                f.write('\n\n')
        return os.path.isfile(filepath)

    def print_csv_to(self, filepath):
        writers = self.statistic.get_writers()
        if os.path.isfile(filepath):
            os.remove(filepath)
        for writer in writers:
            w = Writer(writer, self.statistic.root)
            f = open(filepath, 'a')
            if 'Pressure' in self.statistic.root:
                letters = w.get_letters_pressure()
                line_header = 'Pressure' + ', ' + w.name
            if 'Wacom'in self.statistic.root:
                letters = w.get_letters()
                line_header = 'Wacom' + ', ' + w.name
            if 'Tablet'in self.statistic.root:
                letters = w.get_letters_tablet()
                line_header = 'Tablet' + ', ' + w.name

            to_sort = []
            for i in letters:
                to_sort.append(i)
            for letter in sorted(to_sort):
                f.write(line_header + ', ' + letter + ', ' + str(letters[letter]))
                f.write('\n')
        return os.path.isfile(filepath)
