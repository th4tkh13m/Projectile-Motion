class Object():
    def __init__(self, name, x, y, m) -> None:
        self.name = name
        self.x = x
        self.y = y
        assert m >= 0
        self.m = m

    def getName(self) -> str:
        return self.name

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
        return "Object: " + self.getName + '\n' \
                + "Mass: " + self.getM + '\n' \
                + "Coordinates: <" + str(self.getX) + "," \
                + str(self.getY) + ">"
    def __repr__(self) -> str:
        return str((self.getName, self.getM,
                    self.getX, self.getY))
    
class Ball(Object):
    def __init__(self, name, x, y, m, v, theta) -> None:
        super().__init__(name, x, y, m)
        self.velocity = v
        self.angle = theta

    def getVelocity(self) -> float:
        return self.velocity

    def getAngle(self) -> float:
        return self.angle

    