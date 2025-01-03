from basic import BasicT

class Function(BasicT):
    def __init__(self, type, message, args, return_type):
        super().__init__(type, message)
        self.args = args
        self.return_type = return_type
    
    def printArgumentType(self):
        return self.args
