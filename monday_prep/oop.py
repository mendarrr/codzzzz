# Define a class Rectangle with attributes width and height, and methods area and perimeter.
class Rectangle:
    def __init__(self, width: int, height: int):
        # Your code here
        pass

    def area(self) -> int:
        # Your code here
        pass

    def perimeter(self) -> int:
        # Your code here
        pass

#  Define a class Circle that inherits from a class Shape. The Circle class should have an attribute radius and a method area.
class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius: float):
        # Your code here
        pass

    def area(self) -> float:
        # Your code here
        pass

# Create a base class Animal with an attribute name and a method make_sound(). Create two subclasses, Dog and Cat, that inherit from Animal. Override the make_sound() method for each subclass to represent the sounds they make.
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        pass


#  Create a base class Person with attributes name and age. Create two subclasses, Student and Teacher, that inherit from Person. Override the make_sound() method for each subclass to represent the sounds they make.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def make_sound(self):
        pass

# Create a class Person with private attributes _first_name and _last_name. Implement getter and setter methods for these attributes, ensuring that the setter method validates the input and raises a ValueError if the input is an empty string.
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        pass

    @first_name.setter
    def first_name(self, value):
        pass

    @property
    def last_name(self):
        pass

    @last_name.setter
    def last_name(self, value):
        pass

# Create an abstract class Shape with an abstract method area(). Create two concrete subclasses, Circle and Rectangle, that inherit from Shape and implement the area() method for each subclass.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        pass

# Create a decorator cache_result that can be used to cache the result of a method call in a class. The decorator should store the result of the method call in a class attribute with the same name as the method, but with a _cached_ prefix. If the method is called again with the same arguments, the cached result should be returned instead of recalculating the result.
def cache_result(method):
    pass