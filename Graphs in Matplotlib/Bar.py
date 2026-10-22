import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "DBMS"]
marks = [85, 75, 90, 80]

plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()