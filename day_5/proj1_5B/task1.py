# Python script that observers the temperature fluctuations during a day and calculates the  average

# Define a function for filtering invalid temperature from the list of temps (use *args for passing multiple values into a function
def temp_filter(temps: list) -> list[float]:

    """
    Clear None from the list
    Takes an unfiltered list of temperatues
    Returns a filtered list of termperatures
    """

    return [temp for temp in temps if temp is not None]

# Calculate the average temp during the day
def average_temp(nums: list[float]) -> float:
    
    """
    Calculate the average temp from the temp list
    Takes the temp list
    Returns the average
    """
    res: float =  sum(nums) / len(nums)
    return res

# Formatting the temps (2 decimal places) according to the instructions
def format_temp(num: float) -> str:

    """
    Format the average according to the instructions (2 decimals for floats)
    Returns a string
    """

    return f"{num:.2f}C"

# Input
temps_input: list = [0.5, None, None, 32.9, 22.7, -5.2, None, 15.1]

# Process data by invoking the functions defined above and passing their results to some other functions
filtered_temps: list = temp_filter(temps_input)
average: float = average_temp(filtered_temps)
formatted: float = format_temp(average)

# Show the output
print(f"The list of temperatues during the day according to the thermometer: {temps_input}")
print(f"The filtered list of temperatures: {filtered_temps}")
print(f"The average temperature during the day was {formatted}")


