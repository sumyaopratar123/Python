import array as arr

b = arr.array('d', [2.5, 3.2, 3.3])

print("The new created array is:", end=" ")

for i in range(0, 3):
    print(b[i], end=" ")