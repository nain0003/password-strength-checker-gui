import re
import tkinter as tk
from tkinter import messagebox


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Very Strong 💪", "green"
    elif score >= 3:
        return "Moderate 🙂", "orange"
    else:
        return "Weak ❌", "red"


def evaluate_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, color = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}", fg=color)


# Create window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Password Strength Checker 🔐", font=("Arial", 14, "bold"))
title_label.pack(pady=15)

# Entry field
entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack(pady=10)

# Button
check_button = tk.Button(root, text="Check Strength", command=evaluate_password)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run app
root.mainloop()