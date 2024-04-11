# List Lists are created using square brackets []
# List items are ordered, changeable, and allow duplicate values
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered: When we say that lists are ordered, it means that the items have a defined order, and that order will not change.If you add new items to a list, the new items will be placed at the end of the list.
# Changeable: The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates : Since lists are indexed, lists can have items with the same value: fruits = ["apple", "banana", "cherry", "apple", "cherry"]

# type conversion
id=(1,2,3)
print(type(id))
print(id)
id=list(id)
print(id)


# Indexing
print(id)
print(id[2])

# Slicing
print(id)
print(id[0:2])
print(id[:-1])


#Append
id.append(3)
print(id)


#Insert (index,element)
id.insert(4,5)
print(id)
# Update
id[3]=4
print(id)

# extend
id2=[6,7]
id.extend(id2)
print(id)


# Changeable
# Adding and removing elements
myList = ['a', 'b', 'c', 'd', 'e', 'f']

# Add an element at the end
myList.append('g')
print(myList)

# Insert element at a specific index
# insert(index, value)
myList.insert(3, 'z') # Insertion at the 3rd index
print(myList)

# Delete an element from the end
myList.pop()
print(myList)

# Delete the value at a specific index
del myList[1]
print(myList)

# Allow Duplicates
animal=["monkey","monkey"]

# Python program to demonstrate

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["game", "For", "game"]
print("\nList Items: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['game', 'For'], ['game']]
print("\nMulti-Dimensional List: ")
print(List)


# The list() Constructor
# It is also possible to use the list() constructor when creating a new list

tuple1=("i","love","MSdhoni")
print(type(tuple1))

tuple1=list(tuple1)
print(type(tuple1))

# Size of List

# Creating a List
List1 = []
print(len(List1))
  
# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))


# Adding Elements

a=[]

# add element using append
a.append(0)
print(a)

# add multiple using iterative method
for i in range(1,4):
  a.append(i)
print(a)

# Using Insert Method
a.insert(2,9)
print(a)


# Using extend() method

b=[10,11,12]
a.extend(b)

print(a)

# Accessing elements from the List

print(a[2])

# Access from Multiple 
Multi=[[1,2,3],["hello","hi","bro"]]
print(Multi[1][2])

# Negative indexing

# print the last element of list
print(Multi[1][-1])

# Removing Elements from the List

fruits=["banana","apple","mango","banana","apple","mango"]
print(fruits)

# using remove method
fruits.remove("mango")
print(fruits)

# remove multiple element
fru=["banana","apple"]
for i in range(len(fru)):
  print(fru[i])
  fruits.remove(fru[i])

print(fruits)

# using pop method
fruits.pop(1)
print(fruits)

# Slicing of a List

num=[1,2,3,4,5]

print("printing list from num index 1 to 2 : ",num[1:3])

print("printing all numbers : ",num[:])

print("printing number index from 2 : ",num[2:])

# Negative index List slicing

print("printing number in reverse : ",num[::-1])

print("negative slicing : ",num[-6:-1])





# List Comprehension

# below list contains square of all odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# for understanding, above generation is same as,
odd_square = []

for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x**2)

print(odd_square)

# Iterate over a list in Python

MIB=["hello_world","hello_earth"]
for x in MIB:
  print(x)

# Iterate word
WMIB=["GROW","ALLSOFT"]
for i in WMIB:
  for x in str(i):
    print(x)


# Concatenate two lists in Python

animal_list1=["Bengal Tigers", "IndianLions", "Deer"]
animal_list2=["Pythons",'Wolves', "Foxes", "Bears", "Crocodiles", "WildDogs", "Monkeys","Snakes"]

animals=animal_list1+animal_list2
print(animals)

# Python Membership and Identity Operators.

# in operators
animal_list1=["Bengal Tigers", "IndianLions", "Deer"]

print("Dog" in animal_list1)

print("Deer" in animal_list1)

# is operators
x = 5
if (type(x) is int):
    print("true")
else:
    print("false")


# Built-in functions with List

numbers = [1,2,3,4,5,1,4,5]

# total sum
print("total sum",sum(numbers))

# max in numbers
print("maximum in number",max(numbers))

# min in numbers
print("minimum in number",min(numbers))

# total length 
print("length of numbers",len(numbers))



# Map function
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# syntax : map(function, iterables)

numbers = [2, 4, 6, 8, 10]

# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)   ## it returns a map object
print(squared_numbers_iterator)

# converting to list from map object
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]
     
     