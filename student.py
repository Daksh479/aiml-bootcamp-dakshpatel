# Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, My name is {self.name}")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def greet(self):
        print(f"Hi, I am {self.name}. My roll number is {self.roll}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

person = Person("Daksh")
student = Student("Amit", 50)
teacher = Teacher("Priya", "Python")

person.greet()
student.greet()
teacher.greet()


print("Student Roll:", student.roll)
print("Teacher Subject:", teacher.subject)