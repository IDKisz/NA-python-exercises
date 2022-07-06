# Copy solution from use_classes_create_employee__str__ file.
# Create classes Programmer and Manager derived from Employee. Calling print on such class object should add <position>
# into description built in previous exercise. Consider using super().
# Final string should look like this: '<name>, <last_name>, <position>'

class Employee:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"{self.name}, {self.last_name}"


class Programmer(Employee):
    def __init__(self, name, last_name, position):
        super().__init__(name, last_name)
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.last_name}, {self.position}"


class Manager(Employee):
    def __init__(self, name, last_name, position):
        super().__init__(name, last_name)
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.last_name}, {self.position}"


employee_base = Employee("Karol", "Nowy")
print(employee_base)
employee_prog = Programmer("Jan", "Nowak", "junior")
print(employee_prog)
employee_mana = Manager("Joanna", "Kowalska", "Team Leader")
print(employee_mana)
