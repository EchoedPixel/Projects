import tkinter as tk

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.display = tk.Entry(master, width=30, borderwidth=5, justify=tk.RIGHT, font=('Helvetica', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        self.button_dot = tk.Button(master, text=".", padx=40, pady=20, command=lambda: self.button_click("."))
        self.button_add = tk.Button(master, text="+", padx=40, pady=20, command=self.addition)
        self.button_subtract = tk.Button(master, text="-", padx=40, pady=20, command=self.subtraction)
        self.button_multiply = tk.Button(master, text="X", padx=40, pady=20, command=self.multiplication)
        self.button_divide = tk.Button(master, text="÷", padx=40, pady=20, command=self.division)
        self.button_clear = tk.Button(master, text="CLR", padx=40, pady=20, command=self.clear)
        self.button_delete = tk.Button(master, text="DEL", padx=40, pady=20, command=self.delete)
        self.button_equal = tk.Button(master, text="=", padx=40, pady=20, command=self.equal)

        self.button_1.grid(row=1, column=0, padx=10, pady=5)
        self.button_2.grid(row=1, column=1, padx=10, pady=5)
        self.button_3.grid(row=1, column=2, padx=10, pady=5)

        self.button_4.grid(row=2, column=0, padx=10, pady=5)
        self.button_5.grid(row=2, column=1, padx=10, pady=5)
        self.button_6.grid(row=2, column=2, padx=10, pady=5)

        self.button_7.grid(row=3, column=0, padx=10, pady=5)
        self.button_8.grid(row=3, column=1, padx=10, pady=5)
        self.button_9.grid(row=3, column=2, padx=10, pady=5)

        self.button_0.grid(row=4, column=1, padx=10, pady=5)
        self.button_clear.grid(row=2, column=4, padx=10, pady=5)
        self.button_delete.grid(row=3, column=4, padx=10, pady=5)
        self.button_equal.grid(row=4, column=2, padx=10, pady=5)

        self.button_add.grid(row=4, column=3, padx=10, pady=5)
        self.button_subtract.grid(row=1, column=3, padx=10, pady=5)
        self.button_multiply.grid(row=3, column=3, padx=10, pady=5)
        self.button_divide.grid(row=2, column=3, padx=10, pady=5)
        
        self.button_dot.grid(row=4,column=0, padx=10, pady=5)
        
    def button_click(self, number):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(number))

    def clear(self):
        self.display.delete(0, tk.END)

    def delete(self):
        current = self.display.get()
        if current:
            self.display.delete(len(current)-1, tk.END)

    def addition(self):
        first_number = self.display.get()
        self.function = "addition"
        self.first_number = float(first_number)
        self.display.delete(0, tk.END)

    def subtraction(self):
        first_number = self.display.get()
        self.function = "subtraction"
        self.first_number = float(first_number)
        self.display.delete(0, tk.END)

    def multiplication(self):
        first_number = self.display.get()
        self.function = "multiplication"
        self.first_number = float(first_number)
        self.display.delete(0, tk.END)

    def division(self):
        first_number = self.display.get()
        self.function = "division"
        self.first_number = float(first_number)
        self.display.delete(0, tk.END)

    def equal(self):
        second_number = self.display.get()
        self.display.delete(0, tk.END)

        if self.function == "addition":
            self.display.insert(0, self.first_number + float(second_number))

        if self.function == "subtraction":
            self.display.insert(0, self.first_number - float(second_number))

        if self.function == "multiplication":
            self.display.insert(0, self.first_number * float(second_number))

        if self.function == "division":
            self.display.insert(0, self.first_number / float(second_number))

root = tk.Tk()
gui = CalculatorGUI(root)
root.mainloop()