import tkinter as tk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator (bazileros)")

        self.entry = tk.Entry(root, font=('Arial', 20), bd=5, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('sqrt', 4, 4),
            ('(', 5, 0), (')', 5, 1), ('^', 5, 2), ('C', 5, 3),
        ]

        for btn_text, row, col in buttons:
            btn = tk.Button(root, text=btn_text, font=('Arial', 20), padx=10, pady=10, command=lambda text=btn_text: self.on_click(text))
            btn.grid(row=row, column=col)

    def on_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text == 'sqrt':
            expression = self.entry.get()
            try:
                result = sqrt(eval(expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)

def main():
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
