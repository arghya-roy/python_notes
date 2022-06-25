# multilevel inheritance -

'''In multilevel inheritance, a class inherits from a child class or derived class. 
Suppose three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B. 
In other words, we can say a chain of classes is called multilevel inheritance.'''

# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()