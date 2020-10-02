class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoIsthis(self):
        print("Bird")
    def swim(self):
        print ("Swim Faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoIsthis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

obj= Penguin()
obj.whoIsthis()
obj.swim()
obj.run()