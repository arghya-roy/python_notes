# Method Overloading -
'''
The process of calling the same method with different parameters is known as method overloading. 
Python does not support method overloading. Python considers only the latest defined method even if you overload the method. 
Python will raise a TypeError if you overload the method.
'''

# The following code will give a error -
def mul(a, b):
    c = a * b
    print(c)


def mul(a, b, c):
    d = a * b * c
    print(d)


# the below line shows an error
mul(4, 5)

# This line will call the second product method
mul(3, 7, 5)

######################################################################################################

# So, We can try this in different way - 
class Shape:
    # function with two default parameters
    def area(self, a, b, c=0):
        if c > 0:
            print('Area of Rectangle is:', a * b * c)
        else:
            print('Area of Square is:', a * b)

result1 = Shape()
result1.area(5,2)

result2 = Shape()
result2.area(5,2,3)