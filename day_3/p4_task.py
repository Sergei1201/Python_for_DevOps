# Loops

# Task 1. Counting the number of iterations
n = int(input("Enter a number: "))
original = n # Keep the original number for the output
k = 0
digits_sum = 0;
while n > 0:
    digit = n % 10 # Find the last digit
    digits_sum += digit # Append the last digit the the digit sum
    n = n // 10
    k = k + 1
print(f"The number of digits in the number {original}: {k}")
print(f"The sum of digits in the number {original}: {digits_sum}")

# Task 2. Find the maximum common divider

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
while b != 0:
    a, b = b, a % b

print(f"The max common divider is {a}")

# Task 3. Resource consumption
from random import randint
total = 100
i = 0
while i < 5:
    n = randint(1, 5)
    total = total - n
    i = i + 1
print(f"Resources left: {total}")

# Break
while i < 5:
    n = randint(1, 50)
    total = total - n
    if total < 0:
        total = 0
        break
    i = i + 1
else:
    print("The process has completed")

print(f"Resources left: {total}")

# Task 4. Numbers sum
num = input("Enter a number to calculate the sum of its digits: ")
sumIt = 0
for it in num:
    sumIt += int(it)
print(f"Sum of the digits for number {num} is {sumIt}")

# Final task. Modify the task 3 to use for with range
for i in range(4):
    n = randint(1, 50)
    total = total - n
    if total < 0:
        total = 0
        break
else:
    print("The process has completed")
print(f"Resources left {total}")



