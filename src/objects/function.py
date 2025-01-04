from .basic import BasicT

class Function(BasicT):
    def __init__(self, type, message, args):
        super().__init__(type, message)
        self.args = args
    
    def printArgumentType(self):
        return self.args
