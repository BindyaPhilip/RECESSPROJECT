#area of both rectangle and circle
#When using the math module
import math
class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius
    def calculate_area(self):
        return math.pi*(self.radius**2)
rectangle = Rectangle(4,5)
circle = Circle(4)
print("Area of the circle is:",circle.calculate_area())
print("Area of the rectangle is:",rectangle.calculate_area())
#Without using the math module but using the pi =  3.14159
class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return  3.14159*(self.radius**2)
rectangle = Rectangle(6,4)
circle = Circle(2)
print("Area of the circle is:",circle.calculate_area())
print("Area of the rectangle is:",rectangle.calculate_area())
#Demonstrating abstraction using area of a circle and rectangle
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

rectangle = Rectangle(5, 3)
circle = Circle(2)

print("Area of Rectangle:", rectangle.calculate_area())
print("Area of Circle:", circle.calculate_area())

