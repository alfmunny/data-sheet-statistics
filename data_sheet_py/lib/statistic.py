import os

# a statistic class to include some basic informations for generating corrosponding data sheet, like writers and letters

class Statistic:
    def __init__(self, root):
        self.root = root

    def get_writers(self):
        self.writers = []
        for writer in os.listdir(self.root):
            if not writer[0] == '.':
                if os.path.isdir(os.path.join(self.root, writer)):
                    self.writers.append(writer)
        return self.writers

    def get_letters(self):
        return self
