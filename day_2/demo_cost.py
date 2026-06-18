# Demo cost task
a = 40
y = (a > 5 and a <= 30) * ((a - 5) * 1.2) + (a > 30) * ((a - 30) * 1.5)
print(y)