# Task 1. Using buil-in function in Python
x: float = float(input("Enter the first number: "))
y: float = float(input("Enter the second number: "))
z: float = float(input("enter the third number: "))

max_num: float = max(x, y, z)
print(f"Max: {max_num}")
min_num: float = min(x, y, z)
print(f"Min: {min_num}")
rounded1 = round(x)
rounded2 = round(y)
rounded3 = round(z)
print(f"Rounded: {rounded1} {rounded2} {rounded3}")

# Task 2. Using other built-it function in Python
import math
# help(math)
a: float = float(input("Enter a number: "))
y = math.ceil(math.sqrt(a))
print(f"sqrt(a) = {y}")



