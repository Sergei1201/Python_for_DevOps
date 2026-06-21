# Script that creates random numbers and classifies them as High or Low depending on a threshold defined in a variable
# Using list comprehension instead of for loops

# Import random module
import random

# Set the threshold
threshold = 65

# Create a list of 10 random integers from 1 to 100 using list comprehension technique
numbers = [random.randint(1, 100) for _ in range(10)]

# Test the output 
print(f"The original list of numbers: {numbers}")

# Create the second list based on the threshold
# First create an additional list which will contain "High" or "Low" values
list2 = [] # Initialize an empty list for the beginning

# Iterate over the first array of numbers and fill the list2
for num in numbers:
    if num > threshold:
        list2.append("High")
    else:
         list2.append("Low")

# Show the output
print("The results")
print("=" * 30) # Add 30 "=" for better formatting
# Display the threshold for the user
print(f"The threshold value is {threshold}")
print("=" * 30) # Same as above
print("Numbers ====== High/Low")

# print(numbers) # Testing the output
# print(list2) # Testing the output

# Show the results by displaying items of both lists one by one (numbers and their properties (high or low))
for i in range(len(numbers)):
    print(f"{numbers[i]} ----- {list2[i]}")



