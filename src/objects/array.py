from .basic import BasicT

class Array(BasicT):
    def __init__(self, type, message, size):
        super().__init__(type, message)
        self.size = size
    
    def printArraySize(self):
        return self.size
