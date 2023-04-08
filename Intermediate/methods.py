import random

class Dog:
    info = "My dog name is Juny"

    def __init__(self,name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"Woof Woof My name is {self.name} and my lucky number is {self.lucky_number}")




dog1 = Dog("Juny")
dog2 = Dog("Tuffy")

dog1.bark()
dog2.bark()

#Assignment
"""class Car:

    def __init__(self,brand1,brand2):
        self.brand1 = brand1
        self.brand2 = brand2

    def drive(self):
        print(f"My first fav car is {self.brand1} and Second fav car is {self.brand2}")

car1 = Car("Range Rover Red", "Audi Blue")
car1.drive()"""


#Assignment

"""class Square:
    sides = 4

    def __init__(self):
        self.height = 0

    def area(self):
        return self.height * self.height

my_shape = Square()
my_shape.height = 10
print(my_shape.area())"""
