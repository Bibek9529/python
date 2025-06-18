import tkinter as tk
from tkinter import messagebox

# Predefined credentials
users = {
    "admin": "1234",
    "bibek": "mypassword",
    "guest": "guest123"
}

def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login", f"✅ Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "❌ Invalid username or password.")

# Create window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Username
tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

# Password
tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=20)

# Run the window
root.mainloop()
