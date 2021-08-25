from Engine import Engine
from Beyond12 import Beyond12
from Parser import Parser

import numpy as np


row1 = list("1234567890".upper())
row2 = list("qwertyuiop".upper())
row3 = list("asdfghjkl;".upper())
row4 = list("zxcvbnm,./".upper())
keyboard = np.array([row1, row2, row3, row4])

# Inputs

transformString = ["S3H"]#, "VS-2VVVS1", "H", "S-1", "S-100", "VH", "VHS-1", "S-1V"]
inputString = "HORSE"

# Engine
transformer = Beyond12()
parser = transformer.generateParser()
engine = Engine(keyboard, transformer)

for s in transformString:
    transformations = parser.getListFromString(s)
    for transformation in transformations:
        engine.transformArray(transformation)
        engine.translateString(inputString)
        engine.log()
    engine.reset()

