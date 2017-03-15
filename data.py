import xml.etree.ElementTree as ET
from pathlib import Path
import os

class Data:

    def __init__(self, name, stored):
        self.name = name
        self.stored = stored

    def analyze(self):
        if (type(self.stored) is str):
            try:
                return eval(self.stored)
            except: 
                if (os.path.exists(self.stored)):
                    p = Path(self.stored)
                    return p.stat()
                else:
                    try:
                        root = ET.fromstring(self.stored)
                        l = list()
                        for element in root.iter('*'):
                            l.append(element)
                        return l
                    except:
                        return self.stored
