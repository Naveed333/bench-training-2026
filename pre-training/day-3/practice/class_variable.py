class Employee:
    raise_amount = 1.04
    def __init__(self, first=None, last=None, pay=None):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)




print(Employee.raise_amount)


Employee.raise_amount = 1.05


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
