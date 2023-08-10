import tkinter as tk
import string
import random

def generate_password():
    try:
        password_length = int(length_var.get())
        if password_length <= 0:
            raise ValueError("Password length should be a positive integer.")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_var.set(password)
    except ValueError as e:
        password_var.set("Invalid input. " + str(e))

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create a label and entry for password length
length_label = tk.Label(root, text="Password Length:", font=("Arial", 12))
length_label.pack(pady=10)
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, font=("Arial", 12))
length_entry.pack()

# Create a button to generate a password
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_button.pack(pady=10)

# Create a label to display the generated password
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12))
password_label.pack()

# Start the Tkinter event loop
root.mainloop()
