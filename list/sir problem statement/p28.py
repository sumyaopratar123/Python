scores = [45, 100, 75, 120, 30, 55, 80, 150, 40, 90]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total runs:", sum(scores))
print("Average:", sum(scores) / len(scores))

centuries = len([x for x in scores if x >= 100])
half_centuries = len([x for x in scores if 50 <= x <= 99])

print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
