# Implement a procedure without params in Python
def countgit1():
    n = int(input("Enter a number: "))
    k = 0
    while n > 0:
        n = n // 10
        k = k + 1
    print(f"The amount of digits in the number is {k}")

# Invoke the functions
countgit1()

# Implement a function without params
def countgit2():
    n = int(input("Enter a number: "))
    k = 0
    while n > 0:
        n = n // 10
        k = k + 1
    return k
print(countgit2())

# Function with params
def countdig3(n: int) -> int:
    k = 0
    while n > 0:
        n = n // 10
        k = k + 1
    return k

n: int = int(input("Enter a number: "))
h = countdig3(n)
print(f"The number of digits is {h}")

