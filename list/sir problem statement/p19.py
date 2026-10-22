students = ["sumit", "sai", "suyash"]
print("Total students:", len(students))

name = input("Enter student name: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

name = input("Enter new student name: ")
students.append(name)

name = input("Enter student name to remove: ")

if name in students:
    students.remove(name)

print("Students:", students)
