'''
Here we created a list with objects.
'''
class Customer:
 def __init__(self,name, age):
  self.name = name 
  self.age = age
 def intro(self):
  print("I am", self.name,"and I am", self.age)


C1 = Customer("Nitish",34) 
C2 = Customer("Ankit",45) 
C3 = Customer("Neha",32)
L = [C1,C2,C3]
for i in L:
 i.intro()

