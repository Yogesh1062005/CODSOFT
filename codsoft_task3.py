import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password(length, use_letters, use_digits, use_special_chars):
    # Define possible characters for the password based on user preferences
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Ensure that there's at least one type of character to choose from
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        use_letters = var_letters.get()
        use_digits = var_digits.get()
        use_special_chars = var_special_chars.get()
        password = generate_password(length, use_letters, use_digits, use_special_chars)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Checkbuttons for character types
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special_chars = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=var_letters).grid(row=1, column=0, padx=10, pady=5, sticky='w')
tk.Checkbutton(root, text="Include Digits", variable=var_digits).grid(row=1, column=1, padx=10, pady=5, sticky='w')
tk.Checkbutton(root, text="Include Special Characters", variable=var_special_chars).grid(row=2, column=0, padx=10, pady=5, sticky='w')

# Generate button
btn_generate = tk.Button(root, text="Generate Password", command=on_generate)
btn_generate.grid(row=2, column=1, padx=10, pady=10, sticky='e')

# Entry to display the generated password
entry_password = tk.Entry(root, width=50)
entry_password.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Copy to clipboard button
btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
btn_copy.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
