import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title("Student Data")
root.geometry("650x500")

FILE = "student_data.txt"


# Submit / Save Data
def save_data():
    data = f"{name.get()} | {roll.get()} | {division.get()} | {subject.get()}\n"

    with open(FILE, "a") as file:
        file.write(data)

    name.delete(0, tk.END)
    roll.delete(0, tk.END)
    division.delete(0, tk.END)
    subject.delete(0, tk.END)


# Read Data
def read_data():
    for item in table.get_children():
        table.delete(item)

    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            for line in file:
                data = line.strip().split(" | ")
                table.insert("", "end", values=data)


# Heading
tk.Label(
    root,
    text="Student Information",
    font=("Arial", 18, "bold")
).grid(row=0, column=0, columnspan=2, pady=20)


# Form
tk.Label(root, text="Name").grid(row=1, column=0, padx=20, pady=8)
name = tk.Entry(root, width=30)
name.grid(row=1, column=1)

tk.Label(root, text="Roll No").grid(row=2, column=0, padx=20, pady=8)
roll = tk.Entry(root, width=30)
roll.grid(row=2, column=1)

tk.Label(root, text="Division").grid(row=3, column=0, padx=20, pady=8)
division = tk.Entry(root, width=30)
division.grid(row=3, column=1)

tk.Label(root, text="Subject").grid(row=4, column=0, padx=20, pady=8)
subject = tk.Entry(root, width=30)
subject.grid(row=4, column=1)


# Buttons
tk.Button(root, text="Submit", command=save_data, width=12).grid(
    row=5, column=0, pady=15
)

tk.Button(root, text="Read Data", command=read_data, width=12).grid(
    row=5, column=1, pady=15
)


# Table
table = ttk.Treeview(
    root,
    columns=("Name", "Roll No", "Division", "Subject"),
    show="headings"
)

for col in ("Name", "Roll No", "Division", "Subject"):
    table.heading(col, text=col)
    table.column(col, width=130)

table.grid(row=6, column=0, columnspan=2, padx=20, pady=10)


root.mainloop()