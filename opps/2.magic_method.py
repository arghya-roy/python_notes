''' __init__ is also a magic method, when we create any object then this method would be triggered automatically.
We cannot call magic method from object.

__add__ is a magic method for sum. whenever we use + sign then automatically this method would be executed.

__sub__ is a magic method for sum. whenever we use - sign then automatically this method would be executed.
'''

class Fraction:
 def __init__(self, n, d):
  self.num = n 
  self.den = d
 def __str__(self):
  return "{}/{}".format(self.num,self.den)

 def __add__(self,other):
  temp_num = self.num * other.den + other.num * self.den 
  temp_den = self.den * other.den
  return "{}/{}".format(temp_num,temp_den)

 def __sub__(self, other):
  temp_num = self.num * other.den - other.num * self.den 
  temp_den = self.den * other.den
  return "{}/{}".format(temp_num,temp_den)

 def __mul__(self, other):
  temp_num = self.num * other.num 
  temp_den = self.den * other.den
  return "{}/{}".format(temp_num,temp_den)
####################

x = Fraction(1, 2)
y = Fraction(2, 1)
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)