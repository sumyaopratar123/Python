import array as arr

a = arr.array('i', [1, 2, 3])

print("The new created array is:", end=" ")

for i in range(0, 3):
    print(a[i], end=" ")

a.insert(1, 4)

print("Array after insertion:", end=" ")

for i in a:
    print(i, end=" ")