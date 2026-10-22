marks = [70, 80, 65, 90, 75, 85, 60, 95, 72, 88]
average = sum(marks) / len(marks)

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", average)

print("Above average:", len([x for x in marks if x > average]))
print("Below average:", len([x for x in marks if x < average]))
