numbers = [1,2,5,8,6,4,8,5,6,86,88,75,44,33,44,]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers:", even)
print("Odd numbers:", odd)
