class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, sal):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.sal = sal

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.sal = int(self.sal * self.raise_amt)


    '''used for debugging, logging like things etc.-meant to be seen by devs'''
    def __repr__(self):
        #return a string used to recreate the object > Employee('aman', 'aryn', '80000')
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.sal)
    

    '''redable reprsntn of objs-meant to be seen by end users'''
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)
    
    def __add__(self, other):
        return self.sal + other.sal
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('aman', 'aryn', 80000)
emp_2 = Employee('Test', 'user', 990000)

# print(emp_1)

# print (repr(emp_1))
# print (str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

print(emp_1 + emp_2)
print (len(emp_1))