# Program to print the sequence 1 2 4 8 16 32 ... up to 2^n

n = int(input("Enter the value of n: "))

for i in range(n + 1):
    print(2 ** i, end=" ")