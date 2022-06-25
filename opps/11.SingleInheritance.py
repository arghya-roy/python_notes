# Single Inheritance

'''
In single inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.
'''

# Base class
class Vehicle:
    vehicle_name_without_const = "vehicle_name_without_const"
    def __init__(self):
     self.vehicle_name = "vehicle"
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def __init__(self):
     self.car_name = "car"
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car()


car.Vehicle_info()
#print(car.vehicle_name)   # It will give error because only one constructor will be executed and that will be which has lowest scope.
print(car.vehicle_name_without_const)  # This with execute because it is outside constructor.
print(car.car_name)
car.car_info()