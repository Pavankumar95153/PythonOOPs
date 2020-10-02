class Student:
    def __init__(self, name, age, phn):
        self.name= name
        self.age= age
        self.phn= phn
obj=Student("Pavan",25,951531652)
print("Student name is {}".format(obj.name))
print("Student age is {}".format(obj.age))
print("Student phn is {}".format(obj.phn))