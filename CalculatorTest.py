import tkinter as tk
from tkinter import messagebox
import math

class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.current_input = ""
        self.operator = None
        self.temp = 0
        self.reset_display = False
        self.display_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        display_label = tk.Label(self.root, textvariable=self.display_var, font=('Arial', 24), bg="white", width=24, height=2, anchor='e')
        display_label.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            ('(', 1), (')', 1), ('C', 1), ('/', 1),
            ('7', 2), ('8', 2), ('9', 2), ('*', 2),
            ('4', 3), ('5', 3), ('6', 3), ('-', 3),
            ('1', 4), ('2', 4), ('3', 4), ('+', 4),
            ('0', 5), ('.', 5), ('=', 5), ('!', 5)
        ]

        for btn_text, row in buttons:
            self.root.grid_rowconfigure(row, weight=1)
            action = lambda x=btn_text: self.on_button_click(x)
            button = tk.Button(self.root, text=btn_text, command=action)
            col = buttons.index((btn_text, row)) % 4
            self.root.grid_columnconfigure(col, weight=1)
            button.grid(row=row, column=col, sticky='nsew')

        for i in range(5):
            self.root.grid_rowconfigure(i+1, pad=10)
            for j in range(4):
                self.root.grid_columnconfigure(j, pad=10)

    def on_button_click(self, value):
        if value in {'+', '-', '*', '/', '()', ')'}:
            if self.reset_display:
                self.current_input = value
                self.reset_display = False
            else:
                self.current_input += value
            self.display_var.set(self.current_input)
        elif value == '!':
            if self.current_input and self.current_input.isdigit():
                try:
                    number = int(self.current_input)
                    result = str(math.factorial(number))
                    self.display_var.set(result)
                    self.current_input = result
                    self.reset_display = True
                except Exception as e:
                    messagebox.showerror("Error", "Invalid input for factorial.")
            else:
                messagebox.showerror("Error", "Factorial requires a positive integer.")
                
        elif value == '=':
            if self.current_input:
                try:
                    result = eval(self.current_input)
                    if isinstance(result, (int, float)):
                        result = round(result, 4)
                    self.display_var.set(result)
                    self.current_input = str(result)
                    self.reset_display = True
                except ZeroDivisionError:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    self.current_input = ""
                    self.display_var.set("0")
                    self.reset_display = False
                except Exception as e:
                    messagebox.showerror("Error", "Invalid operation.")
                    self.current_input = ""
                    self.display_var.set("0")
                    self.reset_display = False
        elif value == 'C':
            self.current_input = ""
            self.display_var.set(self.current_input)
            self.reset_display = False
        else:
            if self.current_input == "0" or self.reset_display:
                self.current_input = value
                self.reset_display = False
            else:
                self.current_input += value
            self.display_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x350")
    app = Calculator(root)
    root.mainloop()
