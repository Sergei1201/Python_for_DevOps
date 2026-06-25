# Implement algorithms as functions for finding the greatest common divider, the max of three nums, and a leap year according to the task instructions

# WRITE FUNCTIONS

# Greatest common divider
def divider(a: int, b: int) -> int:
    
    """
    Calculate the greates common divider for tho nums
    """
    while b != 0:
        a, b = b, a % b
    return a

# Max number
def max_num(a: float, b: float, c: float) -> float:
   
   """
    Find the max 
    """
   if (a >= b) and (a >= c):
        return a
   elif (b >= a) and (b >= c):
        return b
   else:
        return c

# Determining if a year is a leap year
def find_if_leap_year(year: int) -> bool:
    
    """
    Checking if the year is leap
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# The main script of the program
# As the user to choose an algorithm
algorithm: str = input("Press 1 for greates common divider, 2 for the max number, 3 for leap year ")

if algorithm == '1':
    a, b = int(input("a: ")), int(input("b: ")) # Takes input of two nums for finding the greatest common divider
    print(f"The greates common divider: {divider(a, b)}")

elif algorithm == '2':
    a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: ")) #Takes input of 3 nums for finding max
    print(f"The max: {max_num(a, b, c)}")

elif algorithm == '3':
    year: int = int(input("Enter year: ")) # Takes input to determine if a year is a leap year
    print(f"Is the year leap? {find_if_leap_year(year)}")

else:
    print("Invalid input")


