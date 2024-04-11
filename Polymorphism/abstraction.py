# # Abstract classes are classes that cannot be instantiated and are meant to be inherited by other classes.
#  They serve as a blueprint for other classes and define common attributes and methods that the derived classes must implement.
# Abstract classes can have both abstract methods (methods without an implementation) and concrete methods (methods with an implementation).

# # To create an abstract class in Python, we need to import the `ABC` (Abstract Base Class) module from the `abc` package.
#  We can then define abstract methods using the `@abstractmethod` decorator. 
# Any class that inherits from the abstract class must implement all the abstract methods.
from abc import ABC,abstractmethod
class BankApp(ABC):

  def database(self):
    print('connected to database')

  @abstractmethod
  def security(self):
    pass

  @abstractmethod
  def display(self):
    pass

# b=BankApp()  Class Code will be executed but the object cant be intantiated ERROR
  #WE cant make a object of abstract  class.


# javat
#   In the above code, we have defined the abstract base class named Polygon and we also defined the abstract method. This base class inherited by the various subclasses. We implemented the abstract method in each subclass. We created the object of the subclasses and invoke the sides() method. The hidden implementations for the sides() method inside the each subclass comes into play. The abstract method sides() method, defined in the abstract class, is never invoked.   # abstract class  
  
from abc import ABC  
  
class Polygon(ABC):   
  
   # abstract method   
   def sides(self):   
      pass  
  
class Triangle(Polygon):   
  
     
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):   
  
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):   
  
   def sides(self):   
      print("I have 4 sides")   
  
# Driver code   
t = Triangle()   
t.sides()   
  
s = square()   
s.sides()   
  
p = Pentagon()   
p.sides()   
  
k = Hexagon()   
K.sides()   

