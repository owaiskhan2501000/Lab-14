from abc import ABC, abstractmethod

# Abstract Class: Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Interface: Drawable
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Class implementing both Shape and Drawable
class Circle(Shape, Drawable):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        print("Drawing a circle")

# Usage
circle = Circle(5)
print(circle.area())  # Output: 78.5
circle.draw()         # Output: Drawing a circle
