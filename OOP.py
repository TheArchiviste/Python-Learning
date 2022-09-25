## Abstract classes - Abstract Base Classes lib

class Person:
    count = 0   # Class Atribute != Object Atribute

    # The underscores are a convention for methods that are
    # called automatically.
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.hobby = ""
        Person.count += 1   # Refers to the class atribute, "self" refers to the object

    def __del__(self):
        Person.count -= 1

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm from {self.location}")
        if self.hobby:
            print(f'I enjoy {self.hobby}')

class Student(Person):
    def __init__(self, name, location, course=""):
        super().__init__(name, location)
        self.course = course

    def greet(self):
        super().greet()
        if self.course:
            print(f"I'm a student and I study {self.course}.")
        else:
            print(f"I'm a student and I don't know what I am studying yet.")

class Singer:
    def sing(self):
        print("I can sing!")

# The order in which the parent classes appear does matter!
# Python method resolution order!
class MusicsStudent(Student, Singer):
    def __init__(self, name, location, course=""):
        super().__init__(name, location, course)


# General OO Programming.      
jane = Person('Jane', 'London')
jane.hobby = "swimming"
jane.greet()

john = Person('John', 'Edinburgh')
john.greet()

print(f'There are {Person.count} person(s)')

del john

print(f'There are {Person.count} person(s)')

# Inheritance.
alice = Student("Alice", "Beijing", "Compuer Science")
alice.greet()

bob = Student("Bob", "Johannesburg", "Business Management")
bob.greet()

ivan = Student("Ivan", "Plovid")
ivan.greet()

print(f'There are {Person.count} person(s)')

# Multiple Inheritance.
charlie = MusicsStudent('Charlie', "Chennai", "Classical Singing")
charlie.greet()
charlie.sing()
