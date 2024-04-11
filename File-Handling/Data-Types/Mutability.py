# mutable objects can change their state or contents and immutable objects can’t change their state or content.

# Immutable Objects : These are of in-built types like int, float, bool, string, unicode, tuple
# Mutable Objects : These are of type list, dict, set . Custom classes are generally mutable.

# tuples are immutable
tuple1 = (0, 1, 2, 3)
#tuple1[0] = 4
print(tuple1)


# strings are immutable
message = "Welcome to GeeksforGeeks"
#message[0] = 'p'
print(message)

# lists are mutable
color = ["red", "blue", "green"]
print(color)

color[0] = "pink"
color[-1] = "orange"
print(color)