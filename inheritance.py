# Class Relationships
    # Aggregation
    # Inheritance


# Aggregation(Has-A relationship)
# example
class Customer:

  def __init__(self,name,gender,address):
    self.name = name
    self.gender = gender
    self.address = address

  def print_address(self):
    print(self.address._Address__city,self.address.pin,self.address.state)

  def edit_profile(self,new_name,new_city,new_pin,new_state):
    self.name = new_name
    self.address.edit_address(new_city,new_pin,new_state)

class Address:

  def __init__(self,city,pin,state):
      self.__city = city
      self.pin = pin
      self.state = state

  def get_city(self):
    return self.__city

  def edit_address(self,new_city,new_pin,new_state):
    self.__city = new_city
    self.pin = new_pin
    self.state = new_state

add1 = Address('gurgaon',122011,'haryana')
cust = Customer('nitish','male',add1)

cust.print_address()

cust.edit_profile('ankit','mumbai',111111,'maharastra')
cust.print_address()
# method example
# what about private attribute


# Inheritance
# What is inheritance
# Example
# What gets inherited?
# Example

# parent
class User:

  def __init__(self):
    self.name = 'nitish'
    self.gender = 'male'

  def login(self):
    print('login')

# child
class Student(User):

  def __init__(self):
    self.rollno = 100

#   def enroll(self):
    print('enroll into the course')

u = User()
s = Student()

print(s.name)
s.login()
s.enroll()
# well in the above code, the parent class constructor never ran when we created the a child class object because child class has its own constructor.
# so the s.name varibale didnt created in the memory

# constructor example

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 13)
s.buy()

# 1.In above when a object of SmartPhone is created then it execute the parent class constructor <br>
# 2.In below child class constructor executed, so s.brand will give eror for not created in memory
# constructor example 2

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

s=SmartPhone("Android", 2)
s.brand

# child can't access private members of the class

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    #getter
    def show(self):
        print (self.__price)
         #getter
    # def__ show(self):   => it cant be accessed by child class
    #     print (self.__price)

class SmartPhone(Phone):
    def check(self):  #cant acces private var
        print(self.__price) 

s=SmartPhone(20000, "Apple", 13)
s.show() #getting private thing by getter
s.check() #Error
print(s.price)






class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):  
        return self.__num

class Child(Parent):

    def show(self):
        print("This is in child class")

son=Child(100)
print(son.get_num())
son.show()
#Getting private parent method in child class object using getter method.


class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val

son=Child(100,10)
print("Child: Val:",son.get_val())
print("Parent: Num:",son.get_num()) #variable never got created


class A:
    def __init__(self):
        self.var1=100

    def display1(self,var1): #argument variable and the variable used inside method are different
        print("class A :", self.var1) #self.var1 taking value from constructor
class B(A):

    def display2(self,var1):
        print("class B :", self.var1)

obj=B()
obj.display1(200)



class A:
    def __init__(self):
        self.var1=100

    def display1(self,var1): #argument variable and the variable used inside method are different
        self.var1=var1
        print("class A :", self.var1) #self.var1 taking value from argument by above line
class B(A):

    def display2(self,var1):
        print("class B :", self.var1)

obj=B()
obj.display1(200)





