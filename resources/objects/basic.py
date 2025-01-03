from constants import TokenType

class BasicT:
    def __init__(self, type: TokenType, message: str):
        self.token_type = type
        self.left = None
        self.right = None
    
    def printMessage(self) -> str:
        return self.message
    
class BasicI:
    def __init__(self, type: TokenType):
        self.token_type = type
        self.left = None
        self.right = None

    