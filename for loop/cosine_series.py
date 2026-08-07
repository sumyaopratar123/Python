import math

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

cosx = 1
sign = -1

for i in range(2, n + 1, 2):
    term = (x ** i) / math.factorial(i)
    cosx += sign * term
    sign *= -1

print("Value of cos(x) using series =", cosx)
print("Value of cos(x) using math.cos() =", math.cos(x))