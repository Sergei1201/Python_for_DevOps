# Working with strings in Python
string1 = "This is a string"
string2 = " This is a string too"
string3 = string1 + string2 # string concatenation

# String methods
print(len(string1)) # Function: returns the length of the string
print(string1.title()) # Converts to the upper register
print(string1.upper()) # Upper case
print(string1.lower()) # Lower case
print(string1.rstrip()) # Strips spaces at the end of the string
print(string1.lstrip()) # Strips spaces at the beginning of the string
print(string1.strip()) # Strips spaces both at the beginning and at the end of the string
print(string1.strip('T')) # Strips the specific symbols

# String concatenation
string4 = "This is an example string"
# string5 = string4 + 15 # Won't work since Python does not support automatic conversion of numbers to strings
string5 = string4 + str(15) # Casting 15 to string solves the problem
print(string5)

# param1 = 15 + "25" # Won't work, you should manually cast the string to an integer
param1 = 15 + int("25") # Casting "25" to a number solves the problem
print(param1)

# String formatting
a = 1 / 3
print("{:7.3f}".format(a))

a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a,b))
print("{:10.3e} {:10.3e}".format(a,b))
