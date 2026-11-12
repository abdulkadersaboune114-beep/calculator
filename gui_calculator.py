import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill=tk.X, padx=10, pady=10, ipady=10)

root.mainloop()
