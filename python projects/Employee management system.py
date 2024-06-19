class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def addEmployee(self):
        while True:
            name = input("Enter the name: ")
            if name.isalpha():
                break
            else:
                print("Invalid Name. Please enter characters only.")
        while True:
            try:
                age = int(input("Enter the age: "))
                if 0 < age <= 90:
                    break
                else:
                    print("Invalid Age. Please enter a valid age(1-90).")
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                salary = int(input("Enter the salary: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        employee = Employee(name, age, salary)
        self.employees.append(employee)

    def printEmployees(self):
        if not self.employees:
            print("No employees at the moment!")
        else:
            for employee in self.employees:
                print(f"Employee: {employee.name} has age {employee.age} and salary {employee.salary}")

    def delete_employees_by_age(self):
        start = int(input("Enter age from: "))
        end = int(input("Enter age to: "))
        self.employees = [employee for employee in self.employees if not (start <= employee.age <= end)]

    def update_salary_by_name(self):
        name = input("Enter name: ")
        new_salary = int(input("Enter new salary: "))
        for employee in self.employees:
            if employee.name.lower().startswith(name.lower()):
                employee.salary = new_salary
                break
        else:
            print("Error: No employee with such a name")

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def displayMenu(self):
        print("Program Options:")
        print("1) Add a new employee")
        print("2) List all employees")
        print("3) Delete by age range")
        print("4) Update salary given a name")
        print("5) End the program")

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice (from 1 to 5): "))
                if 1 <= choice <= 5:
                    return choice
            except ValueError:
                pass
            print("Invalid input. Try again!")

    def run(self):
        while True:
            self.displayMenu()
            choice = self.get_user_choice()
            if choice == 1:
                self.manager.addEmployee()
            elif choice == 2:
                self.manager.printEmployees()
            elif choice == 3:
                self.manager.delete_employees_by_age()
            elif choice == 4:
                self.manager.update_salary_by_name()
            elif choice == 5:
                break

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()