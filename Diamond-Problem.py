# the diamond problem
# https://stackoverflow.com/questions/56361048/what-is-the-diamond-problem-in-python-and-why-its-not-appear-in-python2
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

# Method resolution order
class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()


class A:
    def do_thing(self):
        print('From A')

class B(A):
    def do_thing(self):
        print('From B')

class C(A):
    def do_thing(self):
        print('From C')

class D(B, C):
    pass

d = D()
d.do_thing()

# Python doesn't have this problem because of the method resolution order.
#  Briefly, when you inherit from multiple classes, if their method names conflict, the first one named takes precedence.
#   Since we have specified D(B, C), B.do_thing is called before C.do_thing
#if class D has its own buy() method then it would have called own method.



class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        return 30

    def m2(self):
        return 40

class C(B):

    def m2(self):
        return 20
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1() + obj3.m1()+ obj3.m2())


class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        val=super().m1()+30
        return val

class C(B):

    def m1(self):
        val=self.m1()+20  #it will call m1 of class C itself hence max depth recursion
        return val
obj=C()
print(obj.m1())