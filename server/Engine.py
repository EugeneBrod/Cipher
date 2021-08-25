from Beyond12 import Beyond12
import numpy as np
import re
import random
import math
import Parser

# WRITTEN BY: EUGENE BRODSKY
# GUID: a62af8a7-c93b-44f2-aeea-fa1901b4ee0a

""" Classes:
        Engine - Represents the grid on which transformations are performed
        Parser -  """


class Engine():

    def __init__(self, array, transformer):
        self.transformer = transformer
        self.array = array
        self.indicies = []
        self.string = ""
        self.transformedArray = np.copy(array)
        self.transformedString = ""
        self.transformationString = ""
    
    def getTransformedArray(self):
        return self.transformedArray

    def getOriginalString(self):
        return self.string
    
    def getTransformedString(self):
        return self.transformedString
    
    def getIndicies(self):
        return self.indicies
    
    def getTransformationString(self):
        print (self.transformationString)
        return self.transformationString

    def transformArray(self, transformation):
        self.transformationString += transformation
        self.transformedArray = self.transformer.transform(transformation, self.transformedArray)
        
    def translateString(self):
        self.setIndiciesOnOriginal()
        self.indiciesToStringOnTransformedArray()

    def resetStringAndIndicies(self):
        self.clearString()
        self.clearIndicies()

    def reset(self):
        self.clearIndicies()
        self.clearString()
        self.clearTransformedArray()
        self.clearTransformedString()
        self.clearTransformationString()

    def clearTransformationString(self):
        self.transformationString = ""

    def resetOriginalArray(self, array):
        self.array = array

    def stringToIndiciesOnOriginal(self, string):
        return self.stringToIndicies(string, self.array)
        
    def stringToIndiciesOnTransformedArray(self, string):
        return self.stringToIndicies(string, self.transformedArray)
        
    # Assuming every character of the input matrix is unique, otherwise remapping the input string
    # is an ill-formed problem.
    def stringToIndicies(self, string, array):
        res = []
        for c in string:
            for i, row in enumerate(array):
                for j, val in enumerate(row):
                    if val == c:
                        res.append((i,j))
        return res
        
    def indiciesToStringOnOriginal(self):
        return self.indiciesToString(self.array)

    def indiciesToStringOnTransformedArray(self):
        self.transformedString =  self.indiciesToString(self.transformedArray)

    def indiciesToString(self, array):
        res = ""
        for i in self.indicies:
            res += array[i[0],i[1]]
        return res

    def setString(self, s):
        self.string = s
        self.transformedString = s
    
    def clearString(self):
        self.string = ""

    def setTransformedString(self, s):
        self.transformedString = s
        
    def clearTransformedString(self):
        self.transformedString = self.string

    def clearTransformedArray(self):
        self.transformedArray = np.copy(self.array)

    def setIndiciesOnOriginal(self):
        self.indicies = self.stringToIndiciesOnOriginal(self.string)

    def setIndiciesOnTransfromedArray(self):
        self.indicies = self.stringtoIndiciesOnTransformedArray(self.string)

    def clearIndicies(self):
        self.indicies = self.stringToIndiciesOnOriginal("")
    

    def log(self):
        print("Hello Beyond12!\n")
        print("Here is the keyboard before the transformation.\n")
        print("________________________________________________\n")
        print(self.array)
        print("\n")
        print("________________________________________________\n")
        print("\n")
        print("After applying the following transformation => " + self.transformationString + ", the keyboard looks like this! \n")
        print("________________________________________________\n")
        print(self.transformedArray)
        print("\n")
        print("________________________________________________\n")
        print("\n")
        print("If you had typed => " + self.string + " on the original keyboard, the same keys would map to => " + self.transformedString + " on the transformed keyboard!.\n")
        print("\n\n Thank you for the assesement Beyond12!\n")

