class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    '''to access email like attrb use @property decorator'''
    @property
    def email(self):
        return '{}.{}@gitmail.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('name deleted')
        self.first = None
        self.last = None

emp_1= Employee('aman', 'aryn')
emp_1.fullname='aman kumar' #cant set attrb >AttributeError: property 'fullname' of 'Employee' object has no setter so setter used
print(emp_1.first)
# print(emp_1.email())
print(emp_1.email) #can access email like attrb
print(emp_1.fullname)

del emp_1.fullname