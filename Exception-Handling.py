# Python Try Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# The try block will generate an exception, because x is not defined
try:
  print(x)
except:
  print("An exception occurred")


#   Many Exceptions

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#   Else block
# You can use the else keyword to define a block of code to be executed if no errors were raised

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#   Finally
# The finally block, if specified, will be executed regardless if the try/except block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


  
# This can be useful to close objects and clean up resources:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

  