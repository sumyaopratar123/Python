Married = input("Married (yes/no):")
Gender = input("Gender (m/f/o):")
age = int(input("Enter age: "))
if Married == "yes":
    print("Insured")
elif Gender == "m" and age > 30:
    print("Insured")
elif Gender == "f" and age > 25:
    print("Insured")
else:
    print("Not Insured")
