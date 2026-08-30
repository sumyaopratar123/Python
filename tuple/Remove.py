tuple1 = (10, 20, 30, 40, 50)

tuple1 = tuple(x for x in tuple1 if x != 30)

print(tuple1)