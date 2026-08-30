t = (10, 20, 30)

print("Tuple:", t)
print("Type:", type(t))
print("ID:", id(t))

# Tuple to List
t = list(t)

print("List:", t)
print("Type:", type(t))
print("ID:", id(t))

# Modify list
t.append(40)

print("After adding:", t)
