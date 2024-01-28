from abc import ABC, abstractmethod, abstractproperty

class Shape(ABC):
    @abstractproperty
    def area(self):
        """Abstract property to get the area of the shape."""
        pass

    @abstractproperty
    def perimeter(self):
        """Abstract property to get the perimeter of the shape."""
        pass

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs):
        """Abstract class method to create a shape."""
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def area(self):
        return self._le
