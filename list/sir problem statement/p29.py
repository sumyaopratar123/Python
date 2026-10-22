temperature = [30, 32, 28, 35, 31, 29, 33, 34, 30, 36]

average = sum(temperature) / len(temperature)

print("Hottest:", max(temperature))
print("Coldest:", min(temperature))
print("Average:", average)

print("Above average:", len([x for x in temperature if x > average]))
print("Below average:", len([x for x in temperature if x < average]))
