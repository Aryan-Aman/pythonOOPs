class Employee:
    '''
    self is instance which automatically takes as 1st argument >emp1>self , emp_2>self
    '''
    def __init__(self, first, last, age, sal):
        self.first = first
        self.last = last
        self.age = age
        self.sal=sal
        self.email= first + '.' + last + "@gits.com"

    
    '''for return full name'''
    def full_name(self):
        print('{} {}'.format(self.first, self.last))

'''
both unique instances having different memory locations
'''
emp_1=Employee('test', 'user', 20, 40000)
emp_2=Employee('test2', 'user2', 34, 56000)

# print(emp_1)
# print(emp_2)

'''
not of use as we are adding these manually so whats use of class-
so we'll use init method above 
'''
# emp_1.first='test1'
# emp_1.last='user'
# emp_1.email='test@gmail.com'
# emp_1.age=25
# emp_1.sal=40000

# emp_2.first = 'test2'
# emp_2.last = 'admin'
# emp_2.email = 'admin@gmail.com'
# emp_2.age = 30
# emp_2.sal = 50000

# print(emp_1.email)
# print(emp_2.email)

'''
to type full name each time > create a method withn class to put this functionality in one place-
same print func as below but change to self will work with all instances 
'''
# print('{} {}'.format(emp_1.first, emp_1.last))

print (emp_1.full_name()) 
'''
can run methods using class name itself-we have to manually pass the instance as args,so will pass emp_1
emp1_.full_name will also do the same thing>dont need to pass self does it automatically
here in print (Employee.full_name(emp_1)) emp_1 passes as self in full_name
'''
print (Employee.full_name(emp_1))