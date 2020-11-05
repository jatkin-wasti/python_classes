# Classes, Objects, and Instantiation
# How to create a class
# Syntax is class NameOfClass:
# Camel casing is used for class names, NOT snake casing

# classes are a way to bring data and functionality together
class Dog:
    # defining a class variable
    animal_kind = "canine"
# defining a class function, or method, self refers to the current class

    def __init__(self, name, colour):  # When instantiating a class we need to include arguments to match the parameters
        self.name = name  # assigns the passed name value to the object being created
        self.colour = colour  # assigns the passed colour value to the object being created

    def bark(self):
        return "woof"


# In order to execute a class we have to create an instantiation of that class: an object
fluffy = Dog("fluffy", "grey")  # Creating (or instantiating) an object of our Dog class
print(fluffy.animal_kind)  # Accessing the class variable animal_kind from our fluffy object
print(fluffy.bark())  # Printing out the returned value from the bark method in our fluffy object
print(fluffy.name)  # Prints out the name stored in the fluffy object

lassie = Dog("lassie", "blonde")  # Creating another object of our Dog class
print(lassie.bark())  # Showcasing that both Dog objects can access the same methods

fluffy.animal_kind = "Big Dog"  # Changing the value held in the class variable
print(fluffy.animal_kind)  # This changes the value for that instance
print(lassie.animal_kind)  # But NOT other instances of that class
