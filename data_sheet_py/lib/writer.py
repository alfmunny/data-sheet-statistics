import os
import json
import collections
import ast
# a writer class to offer the access to the details of the writer.
# like writer's files, words and files

class Writer:
    def __init__(self, name, folder):
        self.name = name
        self.folder = folder

    def words(self):
        return self

    def get_segmented_files(self):
        self.segmented_files = []
        for dirname, dirnames, filenames in os.walk(self.folder + '/' + self.name):
            for filename in filenames:
                if "segmented.json" in filename:
                    self.segmented_files.append((os.path.join(dirname, filename)))
        return self.segmented_files

    def get_letters_files(self):
        self.letters_files = []
        for dirname, dirnames, filenames in os.walk(self.folder + '/' + self.name):
            for filename in filenames:
                if "letters.json" in filename:
                    self.letters_files.append((os.path.join(dirname, filename)))
        return self.letters_files

    def get_letters(self):
        files = self.get_letters_files()
        all_letters = []
        for f in files:
            j = open(f)
            j_data = json.load(j)
            for p in j_data:
                p_data = json.loads(p)
                if len(p_data['label']) == 1:
                    all_letters.append(p_data['label'])
                if not p_data['label'].isalpha():
                    if len(p_data['label']) == 2: 
                        if not p_data['label'][0] == ' ':
                            all_letters.append(p_data['label'])
        list = sorted(all_letters, key=str.lower)
        counter = collections.Counter(list)
        return counter 
        
    def get_letters_pressure(self):
        files = self.get_segmented_files()
        all_letters = []
        #print(files)
        for f in files:
            j = open(f)
            j_data = json.load(j)
            for p in j_data:
                if len(p['label']) == 1:
                    all_letters.append(p['label'])
                if not p['label'].isalpha():
                    if len(p['label']) == 2: 
                        if not p['label'][0] == ' ':
                            all_letters.append(p['label'])
        list = sorted(all_letters, key=str.lower)
        counter = collections.Counter(list)
        return counter

    def get_letters_tablet(self):
        files = self.get_letters_files()
        all_letters = []
        c = 0
        for f in files:
            j = open(f)
            j_data = json.load(j)
            for p in j_data:
                if type(p) is dict:
                    if len(p['label']) == 1:
                        all_letters.append(p['label'])
                    if not p['label'].isalpha():
                        if len(p['label']) == 2: 
                            if not p['label'][0] == ' ':
                                all_letters.append(p['label'])
        l = sorted(all_letters, key=str.lower)
        counter = collections.Counter(l)
        return counter
