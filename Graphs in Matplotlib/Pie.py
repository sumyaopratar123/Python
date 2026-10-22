import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "Other"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()