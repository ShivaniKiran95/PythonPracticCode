import random

class Dog:
    info = "My dog name is Juny"

    def __init__(self,name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name



dog1 = Dog("Juny")
dog2 = Dog("Tuffy")

print(dog1.name)
print(dog2.name)
