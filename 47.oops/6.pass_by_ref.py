'''
Here we can see that we can pass a object inside a function.
'''

class Customer:
 def __init__(self,name,gender):
  self.name = name 
  self.gender = gender


def greet(customer): 
  if customer.gender == "Male":
   print("Hello",customer.name," sir") 
  else:
   print("Hello",customer.name, "ma'am")

cust = Customer("Ankita","Female")
greet(cust)