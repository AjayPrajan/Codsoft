import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Advanced Password Generator", font=("Helvetica", 18))
        title_label.pack(pady=10)

        # Password Length
        length_frame = tk.Frame(self.root)
        length_frame.pack(pady=5)
        tk.Label(length_frame, text="Password Length:").grid(row=0, column=0, padx=5)
        self.length_var = tk.IntVar(value=12)
        length_entry = tk.Entry(length_frame, textvariable=self.length_var, width=5)
        length_entry.grid(row=0, column=1, padx=5)

        # Character Type Options
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=5)
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)

        tk.Checkbutton(options_frame, text="Include Uppercase Letters", variable=self.use_uppercase).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Include Digits", variable=self.use_digits).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Include Special Characters", variable=self.use_special).grid(row=2, column=0, sticky="w")

        # Buttons Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        generate_button = tk.Button(button_frame, text="Generate Password", command=self.generate_password)
        generate_button.pack(side=tk.LEFT, padx=5)
        save_button = tk.Button(button_frame, text="Save to File", command=self.save_to_file)
        save_button.pack(side=tk.LEFT, padx=5)
        copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack(side=tk.LEFT, padx=5)

        # Password Display
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(self.root, textvariable=self.password_var, width=50, state='readonly')
        password_entry.pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        use_uppercase = self.use_uppercase.get()
        use_digits = self.use_digits.get()
        use_special = self.use_special.get()

        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1.")
            return

        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "At least one character type must be selected.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def save_to_file(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Warning", "No password generated to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(password)
            messagebox.showinfo("Success", "Password saved successfully.")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Warning", "No password generated to copy.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()  # Now it stays on the clipboard
        messagebox.showinfo("Success", "Password copied to clipboard.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
