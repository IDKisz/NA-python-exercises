# Copy solution from use_classes_create_employee file.
# Change the class that your previously created in such a way that calling print(empl) will give the same result as
# calling empl.print_info().

class Employee:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    # def print_info(self):
    #     print(f"{self.name}, {self.last_name}")

    def __str__(self):
        return f"{self.name}, {self.last_name}"


empl = Employee("Jan", "Nowak")
# empl.print_info()
print(empl)