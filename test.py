import math
from data import Data

d1 = Data("Regular", "How are you today?")
print(d1.analyze())

d2 = Data("Script", "(4 + 1) * 3")
print(d2.analyze())

d3 = Data("File", "/home/family/Pictures/board.png")
print(d3.analyze())

d4 = Data("XML", "<people><person><firstname>John</firstname><lastname>Smith</lastname><age>34</age></person><person><firstname>Samual</firstname><lastname>Baker</lastname><age>52</age></person></people>")
print(d4.analyze())
