import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    message = message_entry.get("1.0", tk.END).strip()

    if not name or not email or not message:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    print("Form submitted!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    # Clear the form
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    message_entry.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Form")
root.geometry("400x300")

# Labels and Inputs
tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Message").pack(pady=5)
message_entry = tk.Text(root, width=40, height=5)
message_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

# Run the app
root.mainloop()
