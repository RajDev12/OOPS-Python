# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

number=1,2,3   #stored as tuple
x,y,z=number
print(x,y,z)
print(type(number))


# Empty table
B= ()
print(type(B))

data=(1,2,3)
print((type(data)))

# A tuple can contain different data types
MTuple=("hello",1,1.3,True,1+3j)
print(MTuple)
print(type(MTuple))

# Ordered
fruits = ("apple", "banana", "cherry")
print(fruits)
print(type(fruits))

# Duplicates are Allowed
Fruit = ("apple", "banana", "cherry", "apple")
print(Fruit)
print(type(Fruit))

#count method
no=(1,1,1,2,3,4)
print("1 occur",no.count(1),"times")

# Index
print("2 is at index no. : " , no.index(2))

# length
print("leanth of no is:",len(no))