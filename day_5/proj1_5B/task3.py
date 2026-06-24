# Script that creates 2 functions for power calculation of two numbers. One of the functions should apply recursion

# Iterative function
def iterative(base_num: float, power: int) -> float:
    
    """
    Returns the power of a number using iterative approach
    """
    res: int = 1
    for _ in range(power):
        res *= base_num
    return res

# Recursion
def recursion(base_num: float, power: int) -> float:
    
    """
    Using recursion technique to calculate the power of a given number
    """
    
    if power == 0:
        return 1
    return base_num * recursion(base_num, power - 1)

# Input
number: float = 7.5
power: int = 5

# Show the output
print(f"Iterative: {number:.2f} to the power of {power} = {iterative(number, power):.2f}")
print(f"Recursive: {number:.2f} to the power of {power} = {recursion(number, power):.2f}")


