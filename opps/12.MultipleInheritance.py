# Multiple Inheritance -
'''
In multiple inheritance, one child class can inherit from multiple parent classes. So here is one child class and multiple parent classes.
'''

class Person:
    def __init__(self):
     print("person level constrcytor")
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def __init__(self):
     print("company level constrcytor")
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company):
    # def __init__(self):
    #  print("Employee level constrcytor")
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')

# Also here only that constructor will run which have lowest class. If Constructor inside Employee class does't present then 
# constructor of person will run before in lowest scope employee we at first inherit person, then Company. ( class Employee(Person, Company): )