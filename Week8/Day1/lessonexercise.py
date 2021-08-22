# Creating a class:
class Dog():
    def __init__(self, name_of_the_dog):
        print("a new dog has been initialized!")
        print("His name is,", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print(f"{self.name} barks, WAF!")

    def walk(self, number_of_meters):
        print(f"{self.name} has walked {number_of_meters} meters.")

    def rename(self, new_name):
        self.name = new_name

class Person():
    def __init__(self, name, age):
        print("A new person has been initialized!")
        print("His name is,", name, "he is", age, "years old.")
        self.name = name
        self.age = age

class point():
    def __init__(self, x, y): # The goal of the init method here is to define two attributes to the point
        self.x = x
        self.y = y

# Creating an object (you call the class):
shelter_dog = Dog("Rex")
shelter_dog.bark()
other_shelter_dog = Dog("Jim")
other_shelter_dog.rename("Lex")
other_shelter_dog.walk(500)
Person1 = Person("Jimmy", 30)
p = point(3, 4)
# Object: shelter_dog.    Class: Dog()


# Creating an attribute for a object:
shelter_dog.color = "Brown"
# We created a attribute called 'color'.


# Accessing the attributes
print("p.x is:", p.x) # The output will be: "p.x is: 3"
print("p.y is:", p.y) # The output will be: "p.x is: 4"

