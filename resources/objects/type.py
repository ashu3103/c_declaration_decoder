from basic import BasicT

class Type(BasicT):
    def __init__(self, type, message, sub_type):
        super().__init__(type, message)
        self.sub_type = sub_type

    def printSubType(self):
        return self.sub_type