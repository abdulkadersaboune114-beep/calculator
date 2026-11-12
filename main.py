import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill=tk.X, padx=10, pady=10, ipady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(buttons_frame, text=text, font=("Arial", 18), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
