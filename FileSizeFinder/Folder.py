import os
from pathlib import Path

class Folder(object):
    def __init__(self, name):
        self.path = name
        try:
            self.contents = os.listdir(name)
        except:
            pass
        self.parent = self.path.parent
        self.size = 0
        


