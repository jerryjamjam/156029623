
class Student():
    #this is the constructor otherwise known as the initialization
    def __init__(self, name, id):
        self.name = name
        self.id = id
    #this is a method within the class that allows the id to be changed
    def changeID(self, id):
        self.id = id
    #another method within the class that allows the name and id to be printed
    def print(self):
        print("{} - {}".format(self.name, self.id))

jane = Student("jane", 15)
jane.print()
jane.changeID(18)
jane.print()
