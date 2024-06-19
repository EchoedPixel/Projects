from queue import PriorityQueue
        
class Hospital:
    def __init__(self):
        self.specializations = {}

    def add_patient(self, name, specialization, status):
        if specialization not in self.specializations:
            self.specializations[specialization] = []
        if len(self.specializations[specialization]) >= 10:
            print(f"Sorry, specialization {specialization} is full at the moment.\nCannot add patient {name}.")
            return
        if status == 0:
            stats = "normal"
            self.specializations[specialization].append((name, stats))
        elif status == 1:
            num_normal_patients = self.get_num_patients(specialization, "normal")
            if num_normal_patients == 0:
                patients = (name, "urgent")
                self.specializations[specialization].insert(0, patients)
            else:
                self.specializations[specialization].insert(len(self.specializations[specialization]) - num_normal_patients, (name, "urgent"))
        elif status == 2:
            num_normal_patients = self.get_num_patients(specialization, "normal")
            num_urgent_patients = self.get_num_patients(specialization, "urgent")
            if num_normal_patients == 0 and num_urgent_patients == 0:
                self.specializations[specialization].insert(0, (name, "super urgent"))
            elif num_normal_patients == 0:
                self.specializations[specialization].insert(num_urgent_patients, (name, "super urgent"))
            else:
                self.specializations[specialization].insert(len(self.specializations[specialization]) - num_normal_patients - num_urgent_patients, (name, "super urgent"))
        print(f"Patient {name} has been added to the {specialization}.")

    def get_num_patients(self, specialization, status):
        return sum(1 for patient in self.specializations[specialization] if patient[1] == status)

    def get_next_patient(self, specialization):
        if specialization not in self.specializations:
            print("There are no patients at the moment.")
            return
        if len(self.specializations[specialization]) == 0:
            print("There are no patients at the moment.")
            return
        name, status = self.specializations[specialization].pop(0)
        print(f"{name}, please proceed to see the doctor.")

    def remove_patient(self, specialization, name):
        if specialization not in self.specializations:
            print("There are no patients at the moment.")
            return
        for patient in self.specializations[specialization]:
            if patient[0] == name:
                self.specializations[specialization].remove(patient)
                print(f"Patient {name} is leaving. Thank you for using our service.")
                return
        print("There is no patient with such a name in this specialization!")

    def print_all_patients(self):
        if not self.specializations:
            print("There are no patients at the moment.")
            return
        for specialization, patients in self.specializations.items():
            if not patients:
                continue
            print(f"Specialization {specialization}:")
            for patient in patients:
                print(f"Patient: {patient[0]} is {patient[1]}")

    def run(self):
        print("Welcome to the hospital management system!")
        while True:
            print("\nProgram Options:")
            print("1) Add new patient")
            print("2) Print all patients")
            print("3) Get next patient")
            print("4) Remove a leaving patient")
            print("5) End the program")
            choice = input("Enter your choice (from 1 to 5): ")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue

            if choice == 1:
                specialization = input("Enter specialization: ") 
                
                while True:
                    name = input("Enter patient name: ")
                    if name.isalpha():
                        break
                    else:
                        print("Invalid Name. Please enter characters only.")

                
                status = int(input("Enter status (0 normal / 1 urgent / 2 super urgent): "))
                try:
                    status = int(status)
                except ValueError:
                    print("Invalid status. Please enter 0, 1, or 2.")
                    continue

                self.add_patient(name, specialization, status)

            elif choice == 2:
                self.print_all_patients()

            elif choice == 3:
                specialization = input("Enter specialization: ")
                self.get_next_patient(specialization)

            elif choice == 4:
                specialization = input("Enter specialization: ")
                name = input("Enter patient name: ")
                self.remove_patient(specialization, name)
    
            elif choice == 5:
                print("\nThank you!\n")
                break
    
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

hospital = Hospital()
hospital.run()