class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Student Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}"

    def __repr__(self):
        return f"Student(name={self.name!r}, roll_no={self.roll_no}, marks={self.marks})"


s1 = Student("Rahul", 101, 85)
s2 = Student("Priya", 102, 92)

students = [s1, s2]

print(students)