from abc import ABC, abstractmethod

# Animal Abstract Class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

# Concrete Classes
class Dog(Animal):
    def eat(self):
        print("Dog is eating")

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def eat(self):
        print("Cat is eating")

    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def eat(self):
        print("Bird is eating")

    def make_sound(self):
        print("Tweet!")

# Example usage:
dog = Dog()
dog.eat()
dog.make_sound()
