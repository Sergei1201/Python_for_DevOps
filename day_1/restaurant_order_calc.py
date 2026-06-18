# Restaurant order

# Ask the user for the input (the sum of the order)
sum_order = float(input("Enter the sum of the order: "))

# Tax calculation
tax = sum_order * 0.13

# Calculate extra money for a waitress
extra = sum_order * 0.1

# The overall cheque
overall = sum_order + tax + extra

# Show the results with 2 decimal numbers in floats
print("======================")
print("RESTAURANT RECEIPT") 
print("======================")
print(f"Order sum: {sum_order:.2f} rubles")
print(f"Tax: {tax:.2f} rubles")
print(f"Extra for the waitress: {extra:.2f} rubles")
print(f"Overall: {overall:.2f} rubles")

