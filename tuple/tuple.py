tuple1 = (10, 20, 30, 40, 50)

print("Original tuple:", tuple1)

tuple1 = tuple1 + (60,)
print("Add:", tuple1)

tuple1 = tuple1 + (70, 80)
print("Extend:", tuple1)

tuple1 = tuple1[:2] + (25,) + tuple1[2:]
print("Insert:", tuple1)

tuple1 = tuple(x for x in tuple1 if x != 40)
print("Remove:", tuple1)

x = tuple1[-1]
tuple1 = tuple1[:-1]
print("Pop:", tuple1)
print("Popped element:", x)

x = tuple1[2]
tuple1 = tuple1[:2] + tuple1[3:]
print("Pop(index):", tuple1)
print("Popped element:", x)

print("Index of 30:", tuple1.index(30))

tuple1 = tuple1 + (30,)
print("Count of 30:", tuple1.count(30))

tuple1 = tuple(sorted(tuple1))
print("Sort:", tuple1)

tuple1 = tuple(sorted(tuple1, reverse=True))
print("Sort(reverse=True):", tuple1)

tuple1 = tuple1[::-1]
print("Reverse:", tuple1)

tuple2 = tuple1
print("Copy:", tuple2)

tuple1 = ()
print("Clear:", tuple1)

tuple1 = (1, 2, 3, 4, 5)

print("Length:", len(tuple1))
print("Maximum:", max(tuple1))
print("Minimum:", min(tuple1))
print("Sum:", sum(tuple1))

print("Membership:", 3 in tuple1)

print("Not membership:", 10 not in tuple1)

print("Reverse slicing:", tuple1[::-1])

tuple2 = (6, 7, 8)
tuple3 = tuple1 + tuple2
print("Concatenation:", tuple3)

tuple4 = tuple1 * 2
print("Repetition:", tuple4)

print("First element:", tuple1[0])
print("Last element:", tuple1[-1])
