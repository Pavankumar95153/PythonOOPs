class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu= Parrot("blu",25)
pak = Parrot("test",26)

# print("this is my {}".format(blu._class_.species))
print("this is {} and age: {}".format(blu.name,blu.age))