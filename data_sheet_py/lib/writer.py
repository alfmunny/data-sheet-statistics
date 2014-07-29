import os
import json
import collections

# a writer class to offer the access to the details of the writer.
# like writer's files, words and files

class Writer:
    def __init__(self, name, root):
        self.name = name
        self.root = root

    def words(self):
        return self

    def get_letters_files(self):
        self.letters_files = []
        for dirname, dirnames, filenames in os.walk(self.root + '/' + self.name):
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
