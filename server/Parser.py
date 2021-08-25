import re

class Parser:

    def __init__(self, regex):
        self.pattern = re.compile(regex)

    def getListFromString(self, s):
        return self.pattern.findall(s)
    
    def getIterFromString(self, s):
        return self.pattern.finditer(s)