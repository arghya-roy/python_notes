# Access Modifiers in Python

'''
Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. But In Python, 
we don't have direct access modifiers like public, private, and protected. We can achieve this by using single underscore and double underscores.

Access modifiers limit access to the variables and methods of a class. Python provides three types of access modifiers private, 
public, and protected.

Public Member: Accessible anywhere from otside oclass.  self.name = "arghya"
Private Member: Accessible within the class.   self.name = "__arghya"
Protected Member: Accessible within the class and its sub-classes.    self.name = "_arghya"

'''
#######################################################################################################

# Public Member

class Employee:
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    def show(self):
        print("Name: ", self.name, 'Salary:', self.salary)

emp = Employee('Jessa', 10000)
print("Name: ", emp.name, 'Salary:', emp.salary)

emp.show()

#################################################################################################################################

''' protected member - Protected members are accessible within the class and also available to its sub-classes. To define a protected member, 
 prefix the member name with a single underscore _.

Protected data members are used when you implement inheritance and want to allow data members access to only child classes. '''

# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)


###################################################################################################

# private member - 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee('Jessa', 10000)

#print('Salary:', emp.__salary) 
print('Salary:', emp._Employee__salary)

''' The Above code will give error because we cant use print('Salary:', emp.__salary) for private member. but we can use 
# print('Salary:', emp._<className>__salary), But it is not good practice. 
# Because when we use self._salary then by default it would be converted into _<className>__salary '''

# Good practise is -

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def show(self):
        print("Name: ", self.name, 'Salary:', self.__salary)

emp = Employee('Jessa', 10000)
emp.show()


