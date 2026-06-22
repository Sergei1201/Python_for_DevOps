# Task 1. Program that finds the maximum of 3 numbers

# Ask the user for an input
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

# Find the max
if (n1 >= n2 and n1 >= n3):
    max = n1
elif (n2 >= n1 and n2 >= n3):
    max = n2
else:
    max = n3

# Print the max
print(f"The maximum number is {max}")

