class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def studentPhone(self,phoneNumber):
        return print("this is the phn: {} of {} ".format(phoneNumber, self.name))
obj= Student("Pavan",25)
obj.studentPhone(9515316562)