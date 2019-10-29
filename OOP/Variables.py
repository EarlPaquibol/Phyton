class Employee:

    raise_amount = 1.04
    num_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_emps += 1

    def fullname(self):
        return '{} {} {}'.format(self.first, self.last, self.raise_amount*self.pay)

emp_1 = Employee('Pogi', 'Earl', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname())
emp_1.raise_amount = 1.05
print(emp_1.fullname())

print(emp_1.num_emps)
