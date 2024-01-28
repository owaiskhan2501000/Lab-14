from abc import ABC, abstractmethod

# Shape Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Implementation for calculating area of a triangle
        pass

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)
