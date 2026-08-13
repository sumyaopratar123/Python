s = input("Enter a sentence: ")

words = s.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:])

print(" ".join(result))