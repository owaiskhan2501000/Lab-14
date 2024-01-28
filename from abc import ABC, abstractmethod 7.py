from abc import ABC, abstractmethod

# Employee Abstract Class
class Employee(ABC):
    def get_name(self):
        pass

    def get_salary(self):
        pass

    @abstractmethod
    def calculate_pay(self):
        pass

# Concrete Subclasses
class FullTimeEmployee(Employee):
    def calculate_pay(self):
        # Implementation for calculating pay for a full-time employee
        pass

class PartTimeEmployee(Employee):
    def calculate_pay(self):
        # Implementation for calculating pay for a part-time employee
        pass

# Example usage:
full_time_employee = FullTimeEmployee()
part_time_employee = PartTimeEmployee()
