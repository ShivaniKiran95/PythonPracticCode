import random

class Animal:
    info = "A living organism that feeds on organic matter."

    def __init__(self,name):
         print("An animal is created")
         self.name = name

class Dog(Animal):
    info = "A Domesticated carnivorous animal."

    def __init__(self,name):
        super().__init__(name)
        print("A dog is created")
        self.lucky_number = random.randint(1,10)
        self.no_fur = ""


    def bark(self):
        print(f"Woof Woof My name is {self.name} and my lucky number is {self.lucky_number}")

class Dachshund(Dog):

    def __init__(self,name):
        super().__init__(name)
        print("A dachshund is created")


dog1 = Dachshund("Juny")

#Assignment:1
"""class Shape:
    side = 1

class Square(Shape):
    sides = 4

    def __init__(self):
        self.height = 0

    def area(self):
        return self.height * self.height


my_shape = Square()
my_shape.height = 10
print(my_shape.area())"""

#Assignment:2
"""class Vehicle:
    print("Transport from one place to another.")


    def __init__(self,name):
        print("Which vehicle you gonna choose?")
        self.name = name

class Car(Vehicle):
    info = "fourwheeler"

    def __init__(self, name):
        super().__init__(name)
        print(" I choose 4 wheeler")

        self.name = name


    def drive(self):
        print(f"This is my dream car!!")

class Rangerover(Car):

    def __init__(self,name):
        super().__init__(name)
        print("Red RangeRover")


car1 = Rangerover("Red")
car1.drive()"""
