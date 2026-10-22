a = []
for i in range(5):
    a.append(int(input("Enter num: ")))
print("Asc:", sorted(a))
print("Des:", sorted(a, reverse=True))
