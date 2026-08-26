s = input("Enter a sentence: ")

words = s.split()
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)