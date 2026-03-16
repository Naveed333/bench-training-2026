class Employee:
    raise_amount = 1.04

    def __init__(self, first=None, last=None, pay=None):
        self.first = first
        self.last = last
        self.email =  first + '.' + last + '@example.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10


dev_1 = Developer('John', 'Doe', pay=50000)
dev_2 = Developer('Jane', 'Smith', pay=60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.pay)