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

    def print_js_to(self, filepath):
        writers = self.statistic.get_writers()
        if os.path.isfile(filepath):
            os.remove(filepath)
        f = open(filepath, 'a')
        if 'Pressure' in self.statistic.root:
            tail = "Pressure"
            f.write('var Pressure = [')
        if 'Wacom'in self.statistic.root:
            tail = "Wacom"
            f.write('var Wacom = [')
        if 'Tablet'in self.statistic.root:
            tail = "Tablet"
            f.write('var Tablet = [')
        counter_w = 1
        for writer in writers:
            w = Writer(writer, self.statistic.root)
            if 'Pressure' in self.statistic.root:
                letters = w.get_letters_pressure()
            if 'Wacom'in self.statistic.root:
                letters = w.get_letters()
            if 'Tablet'in self.statistic.root:
                letters = w.get_letters_tablet()
            to_sort = []

            f.write('{\nid: \'' + writer + '\', ')
            f.write('\n')
            f.write('labels: [')
            for i in letters.keys():
                to_sort.append(i)
            sorted_list = sorted(to_sort)
            counter_l = 1 

            for letter in sorted_list:
                f.write('{\nid: "' + letter + '",' + '\n'+ 'repeat: ' + str(letters[letter]['sum']) + ',\n' + 'files: [')
                counter_f = 1
                for src in letters[letter].keys():
                    if not 'sum' in src:
                        f.write('{\n' + 'id: \'' + src + '\',' + '\n' + 'repeat:' + str(letters[letter][src]) + '\n}')
                        if counter_f != len(letters[letter]):
                            f.write(',')
                    counter_f += 1
                f.write(']\n}')
                if not counter_l == len(sorted_list):
                    f.write(',')
                counter_l += 1
            f.write(']}')
            if not counter_w == len(writers):
                f.write(',')
            counter_w += 1
        f.write('];')
        f.write('\n')
        f.write('export default ' + tail + ';')
        f.close()
        return os.path.isfile(filepath)
