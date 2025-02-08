class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def speak(self):
        print("My Dog Name is", self.name, "his breed is",self.breed,"and his age is",self.age)

my_Dog = Dog("Saru", "Husky",4)
my_Dog.speak()