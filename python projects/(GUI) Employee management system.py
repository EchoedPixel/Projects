import tkinter as tk
from tkinter import ttk

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def Add_Employee(self, name, age, salary):
        employee = Employee(name, age, salary)
        if not any(emp.name == name for emp in self.employees):
            if name.isalpha():
                if 0 < age <= 90:
                    self.employees.append(employee)
                    print(f"employee {employee.name} has been added.")
                else :
                    print("Invalid Age. Please enter a valid age(1-90).")
            else:
                print("Invalid Name. Please enter characters only.")
        else :
            print("another employee with the same name found enter another name.")

    def print_all_Employees(self):
        if not self.employees:
            print("No employees at the moment.")
        else:
            print("-------------------------------------------")
            for employee in self.employees:
                print(f"{employee.name} has age {employee.age} and salary {employee.salary}.")
            print("-------------------------------------------")

    def DeleteByAge(self, age1, age2):
        while True:
            found = False
            for employee in self.employees:
                if employee.age >= age1 and employee.age <= age2:
                    self.employees.remove(employee)
                    print("all employees from age",age1,"to age",age2,"were removed.")
                    found = True
                    break
            if not found:
                break

    def EditEmployeeSalary(self, name, salary):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                employee.salary = salary
                break
            else:
                continue

class FrontendManager(EmployeeManager):
    def __init__(self):
        super().__init__()

        self.root = tk.Tk()
        self.root.title("Employee Management System")

        self.addlabel = tk.Label(self.root, text="Add Employee:")
        self.addlabel.grid(row=0, column=0, padx=10)
        self.name_label = tk.Label(self.root, text="Name")
        self.name_label.grid(row=1, column=0, padx=10)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, padx=10)

        self.age_label = tk.Label(self.root, text="Age")
        self.age_label.grid(row=2, column=0, padx=10)

        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=2, column=1, padx=10)

        self.salary_label = tk.Label(self.root, text="Salary")
        self.salary_label.grid(row=3, column=0, padx=10)

        self.salary_entry = tk.Entry(self.root)
        self.salary_entry.grid(row=3, column=1, padx=10)

        self.add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=4, column=1, pady=10)

        self.separator_horizontal = ttk.Separator(self.root, orient='horizontal')
        self.separator_horizontal.grid(row=5, column=0, columnspan=3, sticky='ew', pady=(10,10))

        self.separator = ttk.Separator(self.root, orient='vertical')
        self.separator.grid(row=0, column=3, rowspan=12, sticky='ns')

        self.printlabel = tk.Label(self.root, text="Print All Employees:")
        self.printlabel.grid(row=2, column=4, padx=(100,0))
        self.print_button = tk.Button(self.root, text="Print Employees", command=self.print_employees)
        self.print_button.grid(row=3, column=4, padx=(100,0), pady=10)

        self.separator_horizontal = ttk.Separator(self.root, orient='horizontal')
        self.separator_horizontal.grid(row=5, column=3, columnspan=3, sticky='ew', pady=(10,10))

        self.deletelabel = tk.Label(self.root, text="Delete By Age range:")
        self.deletelabel.grid(row=6, column=0, padx=20)

        self.age_label_1 = tk.Label(self.root, text="Age from")
        self.age_label_1.grid(row=7, column=0)

        self.age_entry_1 = tk.Entry(self.root)
        self.age_entry_1.grid(row=7, column=1)

        self.age_label_2 = tk.Label(self.root, text="Age to")
        self.age_label_2.grid(row=8, column=0)

        self.age_entry_2 = tk.Entry(self.root)
        self.age_entry_2.grid(row=8, column=1)

        self.delete_button = tk.Button(self.root, text="Delete by Age", command=self.delete_by_age)
        self.delete_button.grid(row=9, column=1, pady=10)

        self.editsalarylabel = tk.Label(self.root, text="Edit Employee Salary(by name):")
        self.editsalarylabel.grid(row=6, column=4,padx=20)

        self.name_label_2 = tk.Label(self.root, text="Name")
        self.name_label_2.grid(row=7, column=4,padx=10)

        self.name_entry_2 = tk.Entry(self.root)
        self.name_entry_2.grid(row=7, column=5, padx=10)

        self.salary_label_2 = tk.Label(self.root, text="New Salary")
        self.salary_label_2.grid(row=8, column=4)

        self.salary_entry_2 = tk.Entry(self.root)
        self.salary_entry_2.grid(row=8, column=5)

        self.edit_button = tk.Button(self.root, text="Edit Salary", command=self.edit_employee_salary)
        self.edit_button.grid(row=9, column=5, pady=10)

        self.root.mainloop()

    def add_employee(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        salary = int(self.salary_entry.get())
        self.Add_Employee(name, age, salary)

    def print_employees(self):
        self.print_all_Employees()

    def delete_by_age(self):
        age1 = int(self.age_entry_1.get())
        age2 = int(self.age_entry_2.get())
        self.DeleteByAge(age1, age2)

    def edit_employee_salary(self):
        name = self.name_entry_2.get()
        salary = int(self.salary_entry_2.get())
        self.EditEmployeeSalary(name, salary)

run = FrontendManager()
run.run()