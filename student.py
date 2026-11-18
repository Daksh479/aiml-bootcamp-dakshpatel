# student data 

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def add_mark(self, score):
        self.marks.append(score)

    def average(self):
        if not self.marks:
            return 0

        return sum(self.marks) / len(self.marks)

    def highest(self):
        if not self.marks:
            return None

        return max(self.marks)

    def lowest(self):
        if not self.marks:
            return None

        return min(self.marks)



student1 = Student("Rahul", 101)
student2 = Student("Amit", 102)
student3 = Student("Priya", 103)