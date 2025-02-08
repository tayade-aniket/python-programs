# Python OOPs Concepts
    Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. By understanding the core OOP principles (classes, objects, inheritance, encapsulation, polymorphism, and abstraction), programmers can leverage the full potential of Python OOP capabilities to design elegant and efficient solutions to complex problems.

    OOPs is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOPs, object has attributes thing that has specific data and can perform certain actions using methods

## OOPs Concepts in Python
    * Class in Python
    * Objects in Python
    * Polymorphism in Python
    * Encapsulation in Python
    * Inheritance in Python
    * Data Abstraction in Python

### Python Class
    A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

#### Some points on Python class: 
    * Classes are created by keyword class.
    * Attributes are the variables that belong to a class.
    * Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

``` bash
    class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
```

#### Explanation
    * class Dog: Defines a class named Dog.
    * species: A class attribute shared by all instances of the class.
    * __init__ method: Initializes the name and age attributes when a new object is created.


### Python Objects
    An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.
    An object consists of:

    * State: It is represented by the attributes and reflects the properties of an object.
    * Behavior: It is represented by the methods of an object and reflects the response of an object to other  objects.
    * Identity: It gives a unique name to an object and enables one object to interact with other objects.

    Creating an object in Python involves instantiating a class to create a new instance of that class. This process is also referred to as object instantiation.

``` bash
    class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name) 
print(dog1.species)
```

#### Explanation
    * dog1 = Dog(“Buddy”, 3): Creates an object of the Dog class with name as “Buddy” and age as 3.
    * dog1.name: Accesses the instance attribute name of the dog1 object.
    * dog1.species: Accesses the class attribute species of the dog1 object.

### __init__ Method
    __init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.

``` bash
    class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
print(dog1.name)
```

#### Explanation
    * __init__: Special method used for initialization.
    * self.name and self.age: Instance attributes initialized in the constructor.