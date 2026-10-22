import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("File Explorer")
root.geometry("500x400")


def explore():
    folder = filedialog.askdirectory()

    if folder:
        txt.delete(0, tk.END)
        pdf.delete(0, tk.END)
        other.delete(0, tk.END)

        for file in os.listdir(folder):
            if file.endswith(".txt"):
                txt.insert(tk.END, file)
            elif file.endswith(".pdf"):
                pdf.insert(tk.END, file)
            else:
                other.insert(tk.END, file)


tk.Button(root, text="Explore Folder", command=explore).pack(pady=15)

tk.Label(root, text="TXT Files").pack()
txt = tk.Listbox(root, width=50)
txt.pack()

tk.Label(root, text="PDF Files").pack()
pdf = tk.Listbox(root, width=50)
pdf.pack()

tk.Label(root, text="Other Files").pack()
other = tk.Listbox(root, width=50)
other.pack()

root.mainloop()