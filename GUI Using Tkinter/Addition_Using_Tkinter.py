import tkinter as tk

def add():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Sum = " + str(a + b))

root = tk.Tk()
root.title("Addition")
root.geometry("300x250")

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()