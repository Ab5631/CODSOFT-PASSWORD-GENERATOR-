# PASSWORD GENERATOR :

import tkinter as tk
import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if length < (6-10):
        return "Password length must be at least 6-10 characters."
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(password_length_entry.get())
        generated_password = generate_password(length)
        result_label.config(text="Generated Password: " + generated_password)
    except ValueError:
        result_label.config(text="Please enter a valid number for the password length.")

root = tk.Tk()
root.title("Password Generator")

password_length_label = tk.Label(root, text="Password Length:")
password_length_label.pack()

password_length_entry = tk.Entry(root)
password_length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
