num = int(input("Enter a number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num
print("Reversed number =", rev)