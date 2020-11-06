class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return '{}.{}@example.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):


emp_1 = Employee('Saumen', 'Roy')
emp_1.first_name = 'Soma'
print(emp_1.first_name)
print(emp_1.full_name())
print(emp_1.email)
