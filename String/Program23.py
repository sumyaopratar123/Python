s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

if len(result) < len(s):
    print(result)
else:
    print(s)