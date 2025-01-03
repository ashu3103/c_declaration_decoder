from basic import BasicT

class Identifier(BasicT):
    def __init__(self, type, message):
        super().__init__(type, message)
        self.parent = None
