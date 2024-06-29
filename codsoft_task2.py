import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        
        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)


operation_var = tk.StringVar(root)
operation_var.set('+')  
tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=10)
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
