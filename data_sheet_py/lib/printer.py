import sys
import os
sys.path.append('./lib')
from writer import Writer

# A printer class to help printing out the data sheet to some defined destinations
class Printer:
    def __init__(self, statistic):
        self.statistic = statistic 
    
    def print_to(self, filepath):
        writers = self.statistic.get_writers()
        if os.path.isfile(filepath):
            os.remove(filepath)
        for writer in writers:
            w = Writer(writer, self.statistic.root)
            f = open(filepath, 'a')
            f.write(w.name)
            f.write('\n===\n\n')
            letters = w.get_letters()
            to_sort = []
            for i in letters:
                to_sort.append(i)
            for letter in sorted(to_sort):
                f.write('\t' + letter + '\t' + str(letters[letter]))
                f.write('\n\n')
        return os.path.isfile(filepath)
