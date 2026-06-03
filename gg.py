import tkinter as tk
from tkinter import ttk

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="", fg="black")
        bar["value"] = 0
        return

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    score = sum([has_upper, has_lower, has_digit, has_special])

    if length < 6:
        strength, color, val = "Too Short", "red", 10
    elif length < 8 or score <= 1:
        strength, color, val = "Weak", "orange", 30
    elif length < 12 or score <= 2:
        strength, color, val = "Fair", "gold", 55
    elif length < 16 or score <= 3:
        strength, color, val = "Good", "yellowgreen", 75
    else:
        strength, color, val = "Strong", "green", 100

    result_label.config(text=f"Strength: {strength}  ({length} characters)", fg=color)
    bar["value"] = val

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Helvetica", 12)).pack(pady=(20, 5))
entry = tk.Entry(root, show="*", width=35, font=("Helvetica", 12))
entry.pack()
entry.bind("<KeyRelease>", lambda e: check_strength())

bar = ttk.Progressbar(root, length=300, mode="determinate")
bar.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 11))
result_label.pack()

root.mainloop()