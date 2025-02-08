class Dog:
    spacies = "Husky"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Oliver", 4)

print(dog1.name)
print(dog1.age)