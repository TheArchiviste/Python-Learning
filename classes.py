class Person:
    count = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.hobby = ""
        Person.count += 1

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

class MusicsStudent(Student, Singer):
    def __init__(self, name, location, course=""):
        super().__init__(name, location, course)
