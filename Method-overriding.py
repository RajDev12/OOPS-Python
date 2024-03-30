# Method Overriding=Child class can override the methods and attributes of parent class
#when both parent and child class have same method
#object will call that class method whose object it is
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)
s.buy()  #it will override the parent class method
p=Phone(20000, "Apple", 13)
p.buy()  #it will override the child class method
