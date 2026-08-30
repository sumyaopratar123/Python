tuple1 = (10, 20, 30, 40)

index = 2

x = tuple1[index]

tuple1 = tuple1[:index] + tuple1[index + 1:]

print("Tuple:", tuple1)
print("Popped element:", x)