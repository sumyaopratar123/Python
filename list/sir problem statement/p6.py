nums = [25, 10, 45, 5, 30]
larg = nums[0]
small = nums[0]
for num in nums:
    if num > larg:
        larg = num
    if num < small:
        small = num
print("Larg:", larg)
print("Small:", small)
