import math

num = int(input("Enter a number: "))

root = int(math.sqrt(num))

count = 0

for i in range(1, root + 1):
    if root % i == 0:
        count = count + 1

if count == 2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")