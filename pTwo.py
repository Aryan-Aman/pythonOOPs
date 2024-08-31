class Employee:
    '''
    do not have to change manually 1.04 which is hidden/hardcoded in the apply_raise class, we can write it in class variable
    '''
    raise_amount = 1.04
    no_of_employees=0

    def __init__(self, first, last, sal):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.sal = sal
        Employee.no_of_employees+=1 #no self bcz we want no of employees to be same for any instance

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # self.sal = int(self.sal * 1.04)
        '''
        accessing through class (i.e Employee) or instance 
        (i.e self will give ability to change for an instance if we want and also allow any subclass to override that constant if they wanted to )
        '''
        self.sal=int(self.sal* self.raise_amount) 

emp_1 = Employee('test', 'employee', 50000)
emp_2 = Employee('admin', 'Employee', 60000)

# print(emp_1.sal)
# emp_1.apply_raise()
# print(emp_1.sal)

'''
print(emp_1.__dict__) - will not print raise_amount as its not in the list of emp_1 
print(Employee.__dict__) - will print raise_amount as its in the class Employee
'''
print(emp_1.__dict__)

'''
Employee.raise_amount=1.05 > will change raise amt for class and all instances
emp_1.raise_amount=1.05 > will change for particular instance ?why >created raise_amt attr within emp_1
'''
emp_1.raise_amount=1.05
print(emp_1.__dict__)#check
'''
accessing class var through class and instance both,when we are trying to access an attr on an instnc,it'll first check if that instance contains that attrb and
if it doesn't>then it'll see if the class/any class that it inherits from contains that attrb 
'''
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


print(Employee.no_of_employees)