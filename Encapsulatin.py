class Computer:
    def __init__(self):
        self.__maxPrice= 900
    def sell(self):
        print("selling price of the Computer: {}".format(self.__maxPrice))
    def setMaxprice(self,price):
        self.__maxPrice=price

c=Computer()
c.sell()
c.__maxPrice=10000
c.sell()
c.setMaxprice(10000)
c.sell()
