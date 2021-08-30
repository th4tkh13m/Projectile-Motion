import numpy as np

class Object():
    """## Demonstrate the objects on the 2D space ##
    Include the name, x,y-coordinates and mass of the object.
    ### Parameters ###
        name: str. (v >= 0)
            The name of the Object.
        x: float
            The x-coordinate of the Object. 
        y: float
            The y-coordinate of the Object. 
        m: float (m >= 0)
            The mass of the Object (kg). 
    """
    def __init__(self, name: str, x: float,
                 y: float, m: float) -> None:
        assert m >= 0, "Mass must be greater than 0!"
        self.name = name
        self.x = x
        self.y = y
        self.m = m

    def getName(self) -> str:
        """Return the name of the object 
        ### Parameters: ###
            None \n
        ### Return: ###
            name: str
                The name of the object.
        """
        return self.name

    def getX(self) -> float:
        """Return the x-coordinate of the object 
        ### Parameters: ###
            None \n
        ### Return: ###
            x: float
                The current x-coordinate of the object.
        """
        return self.x
    
    def getY(self) -> float:
        """Return the y-coordinate of the object 
        ### Parameters: 
            None \n
        ### Return: 
            y: float
                The current y-coordinate of the object.
        """
        return self.y

    def getM(self) -> float:
        """Return the mass of the object 
        ### Parameters: 
        None
        ### Return: 
        m: float
            The mass of the object (kg).
        """
        return self.m

    def setX(self, x: float) -> None:
        """Set the x-coordinate of the object 
        ### Parameters: 
        x: float
            The x-coordinate of the object \n
        ### Return: 
            None
        """
        self.x = x

    def setY(self, y: float) -> None:
        """Set the y-coordinate of the object 
        ### Parameters: 
            y: float
                The y-coordinate of the object. \n
        ### Return: 
            None
        """
        self.y = y

    def setM(self, m: float) -> None:
        """Set the x-coordinate of the object 
        ### Parameters: 
            m: float
                The mass (kg) of the object. Mass must be greater than or equal to 0. \n
        ### Return: 
            None
        """
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
    """Demonstrate the object which is threw at time t = 0.
    Ball is a subclass of Object class, which has 2 more parameters.
    ### Parameters
        v: float. (v >= 0)
            The magnitude of the initial velocity of the Object.
        theta: float
            The angle of the object's initial velocity. 
    """
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

    def getYVelocity(self) -> float:
        return self.getVelocity() \
                * np.sin(self.getAngle())

    