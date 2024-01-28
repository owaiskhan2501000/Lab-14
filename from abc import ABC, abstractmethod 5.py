from abc import ABC, abstractmethod

# Calculator Interfaces
class Adder(ABC):
    @abstractmethod
    def add(self, x, y):
        pass

class Subtractor(ABC):
    @abstractmethod
    def subtract(self, x, y):
        pass

class Multiplier(ABC):
    @abstractmethod
    def multiply(self, x, y):
        pass

class Divider(ABC):
    @abstractmethod
    def divide(self, x, y):
        pass

# Calculator Class
class Calculator(Adder, Subtractor, Multiplier, Divider):
    def __init__(self, strategy):
        self.strategy = strategy

    def add(self, x, y):
        return self.strategy.add(x, y)

    def subtract(self, x, y):
        return self.strategy.subtract(x, y)

    def multiply(self, x, y):
        return self.strategy.multiply(x, y)

    def divide(self, x, y):
        return self.strategy.divide(x, y)

# Strategies (Concrete Classes implementing the interfaces)
class SimpleImplementation(Adder, Subtractor, Multiplier, Divider):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
