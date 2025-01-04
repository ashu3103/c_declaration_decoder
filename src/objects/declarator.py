from .basic import BasicI


class Declarator(BasicI):
    def __init__(self, type):
        super().__init__(type)
        self.child = None
        self.parent = None
