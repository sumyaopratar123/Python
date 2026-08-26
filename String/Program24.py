s = input("Enter a string: ")

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

most = ""
max_count = 0

for ch in frequency:
    if frequency[ch] > max_count:
        max_count = frequency[ch]
        most = ch

print("Most frequent character:", most)
print("Frequency:", max_count)