# Program that generates a list of 100 random names (English names used), then splits them into 2 lists based on the first letter of the first name

# Import name module
import names

# Generating 100 names and get the first name using the get_first_name() method and list comprehension
names_generated = [names.get_first_name() for _ in range(100)]

# Testing the output
# print(names_generated)

# Split the first names into two list using the list comprehension technique
# Here is the logic: we generate 2 lists using the first letter of the first name (zero element) converted to the upper case in case there are some names which might start with a lower letter, then compare it to the letter M. If it's less than M, include to the first list otherwise include to the second list. That's it
from_A_to_M = [name for name in names_generated if name[0].upper() <= 'M']
the_rest_of_names = [name for name in names_generated if name[0].upper() > 'M']

# Show the results to the user

# Show all names first
print(f"All names: {names_generated}")

# Show the first list from A to M
print(f"Names from A to M: {from_A_to_M}")

# Show the rest of the names
print(f"Names from N to Z: {the_rest_of_names}")

