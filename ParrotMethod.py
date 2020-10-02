class Parrot:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sing(self, song):
        return print("this is {} singing {}".format(self.name,song))
    def dance(self):
        return print("{} is dancing".format(self.name))

blu= Parrot("Pavan",25)
blu.sing("Happy")
blu.dance()