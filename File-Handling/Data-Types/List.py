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