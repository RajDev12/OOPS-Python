# Polymorphism
    # Method Overriding
    # Method Overloading
    # Operator Overloading


# Polymorphism With Function and Objects


class Dog(): 

     def animal_kingdom(self): 

       print("Mammal") 

     def legs(self):

       print("Four") 

class Lizard(): 

     def animal_kingdom(self): 

       print("Mammal") 

     def legs(self): 

       print("Four") 

def function1(obj): 

       obj.animal_kingdom() 

       obj.legs()

obj_dog = Dog() 

obj_lizard = Lizard() 

function1(obj_dog) 

function1(obj_lizard)

# Output
# Mammal

# Four

# Mammal

# Four

# In the above example, the function, function1() takes in an object named obj, which in turn lets the functions call the methods, animal_kingdom() and legs() of both the classes, Dog and Lizard.
#  To do this, we must create the instances of both classes.