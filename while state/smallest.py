n = int(input("Enter n: "))
i = 1
while i <= n:
    num = int(input("Enter number: "))
    if i == 1:
        smallest = num
    elif num < smallest:
        smallest = num
    i = i + 1
print("Smallest =", smallest)