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

# Task 2. Leap year. Design an algorithm to find out if a year is the leap year. Apply the algorithm using several options: 1) if-else conditional 2) elif conditional 3) with the if operator 4) with a special function of the calendar module

import calendar

# Ask the user to enter the year
year: int = int(input("Enter a year: "))

# Method 1. Nested if-else
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            res1 = "Leap year"
        else:
            res1 = "Not leap year"
    else:
        res1 = "Leap year"
else:
    res1 = "Not leap year"

# Method 2. elif
if year % 400 == 0:
    res2 = "Leap year"
elif year % 100 == 0:
    res2 = "Not leap year"
elif year % 4 == 0:
    res2 = "Leap year"
else:
    res2 = "Not leap year"

# Method 3. Ternary operator with if
res3 = "Leap year" if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "Not leap year"

# Method 4. Using Calendar
res4 = "Leap year" if calendar.isleap(year) else "Not Leap Year"

# Show the results
print(f"Using if-else: {res1}")
print(f"Using elif: {res2}")
print(f"Using if: {res3}")
print(f"Using calendar: {res4}")



