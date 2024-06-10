from abc import ABC, abstractmethod

class Point:
    def __init__(self, x=float, y=float):
        self.x = x
        self.y = y


class Shape(ABC, Point):
    
    def __init__(self, name=str, colour=str, x=float, y=float):
        super().__init__(x, y)
        self.name = name
        self.colour = colour
    
    @abstractmethod
    def getArea(self) -> float:
        # return float
        pass
    
    @abstractmethod
    def getCenterPoint(self) -> float:
        # return float
        pass


class Rectangle(Shape):
    def __init__(self, name=str, colour=str, x=float, y=float, height=float, width=float):
        super().__init__(self, name, colour, x, y)
        self.height = height
        self.width = width

    def getArea(self) -> float:
        return self.height * self.width

    def getCenterPoint(self) -> Point:
        centerX = self.x + self.width / 2
        centerY = self.y + self.height / 2
        return Point(centerX, centerY)

    def isSquare(self) -> bool:
        return self.height == self.width


class Circle(Shape):
    def __init__(self, name=str, colour=str, x=float, y=float, radius=float):
        super().__init__(self, name, colour, x, y)
        self.radius = radius

    def getArea(self) -> float:
        import math
        return math.pi * (self.radius ** 2)

    def getCenterPoint(self) -> Point:
        return Point(self.x, self.y)
