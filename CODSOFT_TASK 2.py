import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    try:
        # Retrieve and convert inputs
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        # Perform the selected operation
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Math Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Invalid Operation", "Please select a valid operation.")
            return
        
        # Display the result
        result_var.set(f"{result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
# Input for the first number
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Input for the second number
tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Dropdown menu for selecting the operation
tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
operation_var = tk.StringVar()
operation_var.set("Add")  # Default value
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = ttk.Combobox(root, textvariable=operation_var, values=operations, state="readonly")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result display
tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, state='readonly')
result_entry.grid(row=4, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
