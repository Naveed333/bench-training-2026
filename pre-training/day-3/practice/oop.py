# Python Object-Oriented Programming (OOP)

class Employee:
    def __init__(self, first=None, last=None, email=None):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@example.com' if email is None else email


    def full_name(self):        
       return '{} {}'.format(self.first, self.last)


emp_1 = Employee(first='John', last='Doe', email='john.doe@example.com')
emp_2 = Employee(first='Jane', last='Smith', email='jane.smith@example.com')

print(emp_1.email)
print(emp_2.email)
print(emp_1.full_name())
print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {}'.format(emp_2.first, emp_2.last))


# emp_1.first = 'John'
# emp_1.last = 'Doe'
# emp_1.email = 'john.doe@example.com'
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.email)  


# emp_2.first = 'Jane'
# emp_2.last = 'Smith'
# emp_2.email = 'jane.smith@example.com'
# print(emp_2.first)
# print(emp_2.last)
# print(emp_2.email)  
