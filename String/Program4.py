s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
