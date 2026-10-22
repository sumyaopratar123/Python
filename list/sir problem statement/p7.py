nums = []
for i in range(10):
    num = int(input("Enter a number: "))
    nums.append(num)

    total = sum(nums)
    average = total / 10
    
print("Sum:", total)
print("Average:", average)
