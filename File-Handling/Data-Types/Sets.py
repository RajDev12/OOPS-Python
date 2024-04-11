# Sets are written with curly brackets.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can remove items and add new items.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Empty set
ES={}
print(type(ES))

# A Set can contain different data types
number={1, 2, 1,"hello"}
print(number)
print(type(number))

# Sets are unordered
Fruit = {"apple", "banana", "cherry"}
print(Fruit)
print(type(Fruit))

# Duplicates Not Allowed
Fruit = {"apple", "banana", "cherry", "apple"}
print(Fruit)
print(type(Fruit))

# add
Fruit.add("mango")
print(Fruit)
     