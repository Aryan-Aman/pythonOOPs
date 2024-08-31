class Employee:
    raise_amt=1.04
    def __init__(self, first, last, sal):
        self.first=first
        self.last=last
        self.mail= first + '.' + last + '@codee.com' 
        self.sal=sal

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.sal= int (self.sal * self.raise_amt)

class Developer(Employee):
    raise_amt=1.10
    def __init__(self, first, last, sal,prog_lang):
        '''to let Employee handle first,last and sal(super will pass the args to Employee init method) - 
             we can use parent class name also like > Employee.__init__(self, first, last, sal)
        '''
        super().__init__(first, last, sal)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self, first, last, sal, employee=None): #? didnt pass an empty list here instead of None
        super().__init__(first, last, sal)
        if employee is None :
            self.employee=[]
        else:
            self.employee=employee

    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
        else:
            print('Employee already exists')
    
    def remove_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)
        else:
            print('Employee not found')

    def emp_lst(self):
        for emp in self.employee:
            print(emp.fullname())




# print(help(Developer))



dev_1=Developer('aman', 'aryn', 90000,'python')
# dev_2=Developer('TEST', 'USER', 10000)
dev_2=Employee('TEST', 'USER', 10000)

mgr_1=Manager('boss', 'user', 300000, [dev_1])
print(mgr_1.mail)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.emp_lst()

# print(dev_1.prog_lang)
# print(dev_1.mail)

# print(dev_1.sal)
# dev_1.apply_raise()  
# print(dev_1.sal)

'''returns true '''
print (isinstance(mgr_1, Manager)) 
'''returns true '''
print (isinstance(mgr_1, Employee)) 
'''returns false'''
print (isinstance(mgr_1, Developer)) 