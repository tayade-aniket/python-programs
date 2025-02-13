# Inheritance- It allows one class(called a child class) to inherit attributes and methods from another class 
# (parents of base class)

# Parent Class
class Animal:
    def __init__ (self, name):
        self.name = name
    
    def speak(self):
        return "Some Sound"
    
# Child Class
class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        return "Some Barking"
    
myDog = Dog("Golden")
print(myDog.speak())
print(myDog.bark())