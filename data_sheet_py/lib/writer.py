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
                    if not "delay_corrected" in dirname:
                        self.letters_files.append((os.path.join(dirname, filename)))
        return self.letters_files

    def get_letters(self):
        files = self.get_letters_files()
        all_letters = []
        letters_info = {}
        full_info = {}
        for f in files:
            letters_one_file = []
            j = open(f)
            j_data = json.load(j)
            for p in j_data:
                p_data = json.loads(p)
                letters_one_file = self.filter(p_data, letters_one_file)
                all_letters = self.filter(p_data, all_letters)
            list = sorted(letters_one_file, key=str.lower)
            counter = collections.Counter(letters_one_file)
            letters_info[f] = counter
        list = sorted(all_letters, key=str.lower)
        counter = collections.Counter(list)

        full_info = self.full_info_push(counter, letters_info)

        return full_info
        
    def get_letters_pressure(self):
        files = self.get_segmented_files()
        all_letters = []
        letters_info = {}
        full_info = {}
        for f in files:
            letters_one_file = []
            j = open(f)
            try:
                j_data = json.load(j)
            except ValueError:  # includes simplejson.decoder.JSONDecodeError
                print("Value Error in"),
                print(f)
                continue
            for p in j_data:
                all_letters = self.filter(p, all_letters)
                letters_one_file = self.filter(p, letters_one_file)
            list = sorted(letters_one_file, key=str.lower)
            counter = collections.Counter(letters_one_file)
            letters_info[f] = counter

        list = sorted(all_letters, key=str.lower)
        counter = collections.Counter(list)

        full_info = self.full_info_push(counter, letters_info)

        return full_info 

    def get_letters_tablet(self):
        letters_info = {}
        full_info = {}
        files = self.get_letters_files()
        all_letters = []
        for f in files:
            letters_one_file = []
            j = open(f)
            j_data = json.load(j)
            for p in j_data:
                if type(p) is dict:
                    all_letters = self.filter(p, all_letters)
                    letters_one_file = self.filter(p, letters_one_file)
            list = sorted(letters_one_file, key=str.lower)
            counter = collections.Counter(letters_one_file)
            letters_info[f] = counter
        list = sorted(all_letters, key=str.lower)
        counter = collections.Counter(list)

        full_info = self.full_info_push(counter, letters_info)

        return full_info 

    def filter(self, dic, lis):
        if len(dic['label']) == 1:
            if not dic['label'][0] == ' ':
                lis.append(dic['label'])
        if not dic['label'].isalpha():
            if len(dic['label']) == 2: 
                if not dic['label'][0] == ' ':
                    lis.append(dic['label'])
        return lis

    def full_info_push(self, counter, letters_info):
        full_info = {}
        for c in counter.keys():
            full_info[c] = {}
            full_info[c]['sum'] = counter[c]
            for f in letters_info.keys():
                for letter in letters_info[f].keys():
                    if c == letter:
                        full_info[c][f] = letters_info[f][letter]
                        break
        return full_info
