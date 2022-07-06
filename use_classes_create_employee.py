# Create class Employee which takes name and last_name upon object creation.
# Calling empl.print_info() where empl is an Employee instance, should display string in format:
# '<name>, <last_name>'.

class Employee:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def print_info(self):
        print(f"{self.name}, {self.last_name}")


empl = Employee("Jan", "Nowak")
empl.print_info()