s = input("Enter a string: ")

duplicates = ""

for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates += ch

print("Duplicate characters:", duplicates)