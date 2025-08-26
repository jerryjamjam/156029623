class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("no student name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
#wizard is considered the "super class" when working with inheritance
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard(input("WELL?! "))
student = Student("harry", "griffin")
professor = Professor("severe", "defense")

class Student:
    def __init__(self, name, home):
        self.name = name
        self.home = home

    @classmethod
    def from_csv(cls, data):
        name, home = data.split(",")
        return cls(name.strip(), home.strip())

def main():
    student = Student.from_csv("Harry, Gryffindor")
    print(student.name, student.home)

main()
