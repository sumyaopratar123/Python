a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a < b:
    if a < c:
        print("Smallest =", a)
    else:
        print("Smallest =", c)
else:
    if b < c:
        print("Smallest =", b)
    else:
        print("Smallest =", c)