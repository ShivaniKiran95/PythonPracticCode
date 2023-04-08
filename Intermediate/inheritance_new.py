#Create a class named Person, with firstname and secondname properties, and a printname method:
#class Person:
    #def __init__(self, fname, lname):
        #self.firstname = fname
        #self.lastname = lname

    #def printname(self):
        #print(slef.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
#x = Person("Shivani", "Swathi")
#x.printname()

#Create a class name Student, which will inherit the properties and methods from the Person class:
#class Student(Person):
#    pass

#note: Use the pass keyword when you do not want to add any other properties or methods to the class.

#Use the Student class to create an object, and then execute the printname method:

#x = Student("Nithya", "Pooja")
#x.printname()
#Add the __init__ function to the Student class:
#class Student(Person):
#    def __init__(self, fname, lname):
#note:Add super()function this will make the child class in herit all the methods and properties from it's parent:
#    super().__init__(fname, lname)
#Add a property called graduationyear to the Student class:
#    self.graduationyear = 2019
#Add a year parameter, and pass the correct year when creating objects:
#class Student(Person):
    #def __init__(self, fname, lname,year):
        #super().__init__(fname, lname)
        #self.graduationyear = year

#x = Student("Nithya", "Pooja", 2019)"""
#add a method called welcome to the Student class:
    #def welcome(self):
        #print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__ (fname, lname,)
        self.graduationyear =  year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#x = Person("Shivani", "Swathi")
#x.printname()

x = Student("Nithya", "Pooja", 2019)
x.printname()
x.welcome()
