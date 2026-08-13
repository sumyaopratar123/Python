s = input("Enter a string: ")

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

values = sorted(set(frequency.values()), reverse=True)

if len(values) < 2:
    print("No second most frequent character")
else:
    second = values[1]

    for ch in frequency:
        if frequency[ch] == second:
            print("Second most frequent character:", ch)
            print("Frequency:", second)
            break