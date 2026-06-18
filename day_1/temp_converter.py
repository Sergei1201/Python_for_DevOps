# Write a program that converts Fahrenheit to Celsius and vice versa
print("=====Temperature Converter=====")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

# Ask the user to get a choice
choice = input("Enter your choice: (1 or 2): ")
if choice == '1':
    
    # Convert Fahrenheit to Celsius
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print(f"Fahrenheit {fahrenheit}F = {celsius}C in Celsius")

elif choice == '2':

    # Convert Celsius to Fahrenheit
    celsius = float(input("Enter temperatue in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Celsius {celsius}C = {fahrenheit}F in Fahrenheit")

else:
    print(f"Invalid choice. You should type 1 or 2")

