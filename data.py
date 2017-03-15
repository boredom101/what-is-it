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
                self.result = eval(self.stored)
                return self.result
            except: 
                if (os.path.exists(self.stored)):
                    p = Path(self.stored)
                    self.result = p.stat()
                    return self.result
                else:
                    try:
                        root = ET.fromstring(self.stored)
                        l = list()
                        for element in root.iter('*'):
                            l.append(element)
                        self.result = l
                        return self.result
                    except:
                        self.result = self.stored
                        return self.stored
