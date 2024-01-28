
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @classmethod
    def create(cls, name):
        # Class method to create a shape with a given name
        return cls(name)

# Concrete Subclasses
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def area(self):
        return 3.14 * self._radius * self._radius

    def perimeter(self):
        return 2 * 3.14 * self._radius

    @classmethod
    def create(cls, name, radius):
        # Overriding the class method to create a Circle with a given radius
        return cls(name, radius)

# Example Usage:
circle = Circle.create("Circle1", 5)
print(circle.name)      # Output: Circle1
print(circle.radius)    # Output: 5
print(circle.area())     # Output: 78.5
print(circle.perimeter()) # Output: 31.4
