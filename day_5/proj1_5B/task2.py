# Python script for writing a function that takes any number of args, returns a tuple from two lists (negative and non-negative sorted in the ascending and descending orders respectively)

# Function that performs actions described above
def sort_nums(*args: float) -> tuple:
    
    """
    Function takes any numbrer of args (numbers) and returns a tuple
    """
    
    nums_negative: list = sorted([arg for arg in args if arg < 0], reverse=True) # Returns a new list sorted in the descend order
    nums_positive: list = sorted([arg for arg in args if arg >= 0]) # REturns a new list sorted in the ascend order by default
    return (nums_negative, nums_positive)

# Input
nums: list = [2.5, 3.755, 9.107, 1009,3229, -322.99, 0, 0.12345, -999.992]
output: tuple = sort_nums(*nums) # unpack the list into arguments

# Formatted output according to the instructions
negatives: list = [f"{num:.2f}" for num in output[0]] # format the first element of the tuple (output[0] which is a list)
positives: list = [f"{num:.2f}" for num in output[1]] # format the second elmeent of the tuple (otuput[1] which is a list as well)

# Show the results to the user
print("Negative numbers sorted in the descending order: ")
print("-" * 60)
print(negatives)
print("Positive numbers sorted in the ascending order: ")
print("-" * 60)
print(positives)


