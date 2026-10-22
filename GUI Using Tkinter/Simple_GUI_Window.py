import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

label = tk.Label(root, text="Hello Python!")
label.pack(pady=30)

button = tk.Button(root, text="Click Me")
button.pack()

root.mainloop()