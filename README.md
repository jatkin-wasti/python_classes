# Classes
## What are classes
- Practically everything in Python is an Object
- Objects are instances of a Class
- Useful to make many object using a single template
- Encapsulates functionality into a single place
- Classes are the main factor that is used to implement the four pillars found below
### Creating a class
- Syntax is
```
class ClassName:
    class_variables_here
    def class_function(self):
        return something
```
- A real example is
```
class Dog:
# defining a class variable
    animal_kind = "canine"
# defining a class function, or method, self refers to the current class
    def bark(self):
        return "woof"
```
### Initialising a class
- Syntax is
```
def __init__(self, parameter1, parameter2):
    self.parameter1 = parameter1
    self.parameter2 = parameter2
```
- When creating instances of this class, we must pass in arguments that match up
with these parameters
- This is useful to assign values to object properties that are important for that class
## OOP (Object Oriented Programming)
### Four pillars
#### Abstraction
- Reduces complexity and isolate impact of changes
- Showing only what's necessary of an object the other parts of your program
#### Encapsulation
- Reduces access and increases reusability 
- Wrapping up data (class variables) and functionality (methods) together into a single place
#### Inheritance
- Eliminates redundant code
- An object can acquire the properties of another (super) object
- This helps to reuse, customise and enhance existing code
- We can use all functions and variables from parent class
#### Polymorphism (morph - form, poly - many) 
- Refactor code or case statements 
- Refers to a programming languages ability to process objects differently depending on their data type 
or class
- More specifically it is the ability to redefine methods for derived classes
- It allows us to change behaviours or attributes/variables
### Creating an object
- Syntax is ```object_name = ClassName()```
- An example is 
```
fluffy = Dog()  # Creating an object of our Dog class
```
### Interactions between Classes and Objects
- To access a class function (method) from an object the syntax is
```
object_name.class_function()
```
- If you make a change to a class, it will carry those changes over to any instances of that class
- Or any other classes that inherit from it
- If you change class values for a specific object i.e. using ```object_name.class_variable = new_value```, it will NOT affect other instances of that class
## Tasks
### Task 1
- Create a Cat class with one function that returns a "Meow"
- Include 2 class variables, 3 objects
- Display all information with each object
- Change the class variable values in each object and display
### Solution
- Class definition
```
class Cat:  # Creating the Cat class with variables for the cat's owner and fur colour
    owner = "Derek"
    colour = "black"
    def meow(self):  # Giving the Cat object the ability to speak
        return "Meow"
```
- Creating the objects and outputting their class variables
```
# Creating an instance of the Cat class and using an fstring to output its class variables
mittens = Cat()
print(f"Mittens is a {mittens.colour} cat, belonging to {mittens.owner}. Mittens says: ")
print(mittens.meow())
# Creating another instance of the Cat class, changing its class variables and using an fstring to output them
spotty = Cat()
spotty.owner = "Sally"
spotty.colour = "tortoiseshell"
print(f"Spotty is a {spotty.colour} cat, belonging to {spotty.owner}. Spotty says: ")
print(spotty.meow())
# Creating another instance of the Cat class, changing its class variables and using an fstring to output them
frumpkin = Cat()
frumpkin.owner = "Caleb"
frumpkin.colour = "orange"
print(f"Frumpkin is a {frumpkin.colour} cat, belonging to {frumpkin.owner}. Frumpkin says: ")
print(frumpkin.meow())
```