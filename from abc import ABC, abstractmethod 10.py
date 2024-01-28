from abc import ABC, abstractmethod

# Interface 1: Drawable
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Interface 2: Clickable
class Clickable(ABC):
    @abstractmethod
    def click(self):
        pass

# Class implementing both interfaces
class Button(Drawable, Clickable):
    def draw(self):
        print("Drawing a button")

    def click(self):
        print("Button clicked")

# Usage
button = Button()
button.draw()  # Output: Drawing a button
button.click()  # Output: Button clicked
