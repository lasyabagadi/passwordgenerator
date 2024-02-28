import tkinter as tk
from tkinter import StringVar, IntVar
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")

        self.length_var = StringVar()
        self.uppercase_var = IntVar()
        self.lowercase_var = IntVar()
        self.numbers_var = IntVar()
        self.symbols_var = IntVar()

        self.init_ui()

    def init_ui(self):
        tk.Label(self, text="Password Length:").pack()
        length_entry = tk.Entry(self, textvariable=self.length_var)
        length_entry.pack()

        tk.Checkbutton(self, text="Include Uppercase Letters", variable=self.uppercase_var).pack()
        tk.Checkbutton(self, text="Include Lowercase Letters", variable=self.lowercase_var).pack()
        tk.Checkbutton(self, text="Include Numbers", variable=self.numbers_var).pack()
        tk.Checkbutton(self, text="Include Symbols", variable=self.symbols_var).pack()

        generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        generate_button.pack()

        tk.Label(self, text="Generated Password:").pack()
        self.password_output = tk.Entry(self, state="readonly")
        self.password_output.pack()

    def generate_password(self):
        length = int(self.length_var.get())
        include_uppercase = bool(self.uppercase_var.get())
        include_lowercase = bool(self.lowercase_var.get())
        include_numbers = bool(self.numbers_var.get())
        include_symbols = bool(self.symbols_var.get())

        chars = ''
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_lowercase:
            chars += string.ascii_lowercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += string.punctuation

        if not chars:
            self.password_output.config(state="normal")
            self.password_output.delete(0, tk.END)
            self.password_output.insert(0, 'Please select at least one character type.')
            self.password_output.config(state="readonly")
        else:
            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_output.config(state="normal")
            self.password_output.delete(0, tk.END)
            self.password_output.insert(0, password)
            self.password_output.config(state="readonly")

app = PasswordGenerator()
app.geometry('300x300')
app.mainloop()