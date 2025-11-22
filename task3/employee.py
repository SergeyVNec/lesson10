class Employee:
    """Class that represents an employee with name and salary."""
    
    employee_count = 0  # counter of employees

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def show_info(self):
        """Show information about some employee."""
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def show_total_employees(cls):
        """Show total employee."""
        print(f"Total employees: {cls.employee_count}")


print("Base class:", Employee.__base__)
print("Namespace (dict):", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)
