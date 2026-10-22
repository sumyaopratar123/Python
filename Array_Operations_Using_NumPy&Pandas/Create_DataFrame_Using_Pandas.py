import pandas as pd

data = {
    "Name": ["Amit", "Sumit", "Rahul"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)
print("Average Marks:", df["Marks"].mean())