from constants import TokenType

class BasicT:
    def __init__(self, type: TokenType, message: str):
        self.token_type = type
        self.left: BasicT = None
        self.right: BasicT = None
        self.message = message
    
    def printMessage(self) -> str:
        return self.message
    
class BasicI:
    def __init__(self, type: TokenType):
        self.token_type = type
        self.left: BasicT = None
        self.right: BasicT = None

    