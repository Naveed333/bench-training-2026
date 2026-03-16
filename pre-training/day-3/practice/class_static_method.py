class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first=None, last=None, pay=None):
        self.first = first
        self.last = last
        self.email =  first + '.' + last + '@example.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        print('class method called',cls)
        cls.raise_amount = amount 


    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('John', 'Doe', pay=50000)
emp_2 = Employee('Jane', 'Smith', pay=60000)


import datetime
my_date = datetime.date(2024, 6, 1)
print(Employee.is_workday(my_date)) 


emp_str_1 = 'John-Doe-50000'
emp_str_2 = 'Jane-Smith-60000'
emp_str_3 = 'Bob-Smith-70000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_2.email)
print(new_emp_3.email)
