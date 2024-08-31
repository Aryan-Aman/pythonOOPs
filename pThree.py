import datetime #for static method

class Employee:

    no_of_employee=0
    raise_amt=1.04

    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.email= first + '.' + last + "@gits.com"
        self.sal=sal

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.sal=int (self.sal* self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

    '''no need for parsing the strings anymore as from_strng alternative constructor '''
    @classmethod
    def from_strng(cls, emp_str):
        first, last, sal = emp_str.split('-')
        return cls(first, last, sal)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True

    
emp_1=Employee('Aman', 'Arya', 90000)
emp_2=Employee('Test', 'kumar', 80000)

'''for classmethods from_strng'''
emp_str_1='aman-arya-76000'
empt_str_2='test-kumar-8000'
emp_str_3='tesst-singh-800'
# first, last, sal = emp_1_str.split('-')
# new_empl_1=Employee(first, last, sal)
new_emp_2=Employee.from_strng(empt_str_2)
print(new_emp_2.email)
print(new_emp_2.sal)

'''automatically takes cls'''
# Employee.set_raise_amt(1.08)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

'''for static method'''
my_date= datetime.date(2024, 9, 1)
print(Employee.is_workday(my_date))