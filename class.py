import numpy as np

class Object():
    def __init__(self, name: str, x: float,
                 y: float, m: float) -> None:
        assert m >= 0, "Mass must be greater than 0!"
        self.name = name
        self.x = x
        self.y = y
        self.m = m

    def getName(self) -> str:
        return self.name

    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y

    def getM(self) -> float:
        return self.m

    def setX(self, x: float) -> None:
        self.x = x

    def setY(self, y: float) -> None:
        self.y = y

    def setM(self, m: float) -> None:
        assert m >= 0, "Mass must be greater than 0!"
        self.m = m

    def __str__(self) -> str:
        return "Object: " + str(self.getName()) + '\n' \
                + "Mass: " + str(self.getM()) + '\n' \
                + "Coordinates: <" + str(self.getX()) + "," \
                + str(self.getY()) + ">"
 
    def __repr__(self) -> str:
        return str((self.getName(), self.getM(),
                    self.getX(), self.getY()))
## TEST CLASS ##
# Ball = Object("Ball", 0, 0, -100)
# print(Ball.getX())
# print(Ball)
    
class Ball(Object):
    def __init__(self, name, x, y, m, v, theta) -> None:
        super().__init__(name, x, y, m)
        self.velocity = v
        self.angle = theta

    def getVelocity(self) -> float:
        return self.velocity

    def getAngle(self) -> float:
        return self.angle

    def getXVelocity(self) -> float:
        return self.getVelocity() \
                * np.cos(self.getAngle())

    