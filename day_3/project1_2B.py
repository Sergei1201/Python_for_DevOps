# Program that creates three lists, combines them together using zip(), and display the output on the screen

# Create list 1: food items
food_items: str = ["Soup", "Pizza", "Salad", "Ice Cream", "Bread", "Sausages", "Dessert", "Juice", "Beer", "Wine"]

# Create list 2: Cost
costs: float = [150.9, 260.0, 500.9, 50.5, 359.0, 670.5, 421.5, 200.0, 152.5, 925.5 ]

# Create list 3: Employee code (3-digit)
emp_codes: int = [201, 302, 404, 609, 700, 232, 950, 111, 545, 600]

# Combine the lists together using the zip() function
combined: list = list(zip(food_items, costs, emp_codes)) # Returns a list of tuples

# Display the result onto the screen
print("Sales report")
print("=" * 30) # Add 30 symbols =
print("Food Items Cost(Rub) Emp Code")
print("-" * 30) # Add 30 symbols -

# Iterate over the list of tuples to display the results using the for loop
for food_items, costs, emp_codes in combined:
    print(f"{food_items} {costs}rub {emp_codes}")

# print(combined) # Testing the output



