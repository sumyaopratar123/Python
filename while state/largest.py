n = int(input("Enter n: "))

i = 1
largest = 0

while i <= n:
    num = int(input("Enter number: "))
    if i == 1 or num > largest:
        largest = num
    i = i + 1

print("Largest =", largest)