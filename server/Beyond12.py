from Parser import Parser
import numpy as np

class Beyond12:

    def transform(self, transformation, array):
            tranformIdentier = transformation[0]
            if tranformIdentier == 'S':
                array = self.shiftArray(transformation, array)
            if tranformIdentier == 'V':
                array = self.flipArrayVertically(array)
            if tranformIdentier == 'H':
                array = self.flipArrayHorizontally(array)
            return array

    def shiftArray(self, transformation, array):
        shiftAmmount = int(transformation[1:])
        '''
        for i, arr in enumerate(array):
            array[i] = np.roll(array[i], shiftAmmount)
        '''
        array = np.roll(array, shiftAmmount)
        return array

    def flipArrayVertically(self, array):
        array = np.flipud(array)
        return array

    def flipArrayHorizontally(self, array):
        array = np.fliplr(array)
        return array

    def generateParser(self):
        regex = "[HV]|S-?[0-9]+"
        parser = Parser(regex)
        return parser
