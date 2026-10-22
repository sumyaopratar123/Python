salary = [25000, 55000, 40000, 60000, 28000, 70000]
average = sum(salary) / len(salary)

print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", average)

print("Above 50000:", len([x for x in salary if x > 50000]))
print("Below 30000:", len([x for x in salary if x < 30000]))
