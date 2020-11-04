# Task: Create a Cat class with one function that returns a "Meow"
# Include 2 class variables, 3 objects
# Display all information with each object
# Change the class variable values in each object and display

class Cat:  # Creating the Cat class with variables for the cat's owner and fur colour
    owner = "Derek"
    colour = "black"
    def meow(self):  # Giving the Cat object the ability to speak
        return "Meow"


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
