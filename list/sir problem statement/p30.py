names = ["Rahul", "Amit", "Priya"]
ages = [20, 25, 30]

names.append("Ravi")
ages.append(35)

names.remove("Amit")

search = "Rahul"

if search in names:
    print("Patient found")
else:
    print("Patient not found")

for i in range(len(names)):
    print(names[i], "-", ages[i])

print("Total patients:", len(names))
