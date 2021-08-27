class Object():
    def __init__(self, name, x, y, m) -> None:
        self.name = name
        self.x = x
        self.y = y
        assert m >= 0
        self.m = m

    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y

    def getM(self) -> float:
        return self.m

    def setX(self, x) -> None:
        self.x = x

    def setY(self, y) -> None:
        self.y = y

    def setX(self, m) -> None:
        self.m = m

    def __str__(self) -> str:
        pass