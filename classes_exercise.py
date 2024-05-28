from abc import ABC,abstractmethod

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape(Point, ABC):
    
    def __init__(self, name=str, colour=str, x, y):
        super().__init__(x, y)
        self.name = name
        self.colour = colour
    
    @abstractmethod
    def getArea(self):
        # return float
        pass
    
    @abstractmethod
    def getCenterPoint(self):
        # return float
        pass


class Rectangle(Shape):
    def __init__(self, name=str, colour=str, x, y, height, width):
        super().__init__(self, name, colour, x, y)
        self.height = height
        self.width = width

    def isSquare(height, width):
        # return bool
        if height == width:
            return True
        else:
            return False


class Circle(Shape):
    def __init__(self, name=str, colour=str, x, y, height, width):
        super().__init__(self, name, colour, x, y)
        self.height = height
        self.width = width

    