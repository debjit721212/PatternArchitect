# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name
        
# Double Inheritance 
class Employee(Person):
    def __init__(self, name,emp_id):
        super().__init__(name)
        self.emp_id = emp_id
        
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeeJob(Employee,Job):
    def __init__(self, name,emp_id,salary,role):
        Employee.__init__(self,name,emp_id)
        Job.__init__(self,salary)
        self.role = role
        
# empjob = EmployeeJob(name="John", emp_id=101, salary=50000, role="Developer")
# print(empjob.name)
# print(empjob.emp_id)
# print(empjob.salary)
# print(empjob.role)

class AssitentManager(EmployeeJob):
    def __init__(self, name, emp_id, salary, role,dauty):
        # super().__init__(name, emp_id, salary, role)
        EmployeeJob.__init__(self,name,emp_id,salary,role)
        self.dauty = dauty

ass = AssitentManager(name="Deb",emp_id=1,salary=1000000000,role="software Engineer",dauty="code")
print(ass.dauty)
print(ass.name)
"""
for super() no need to pass self 
But for one class init Employee.__init__(self,name,emp_id) we need to pass self as a parameter 
"""