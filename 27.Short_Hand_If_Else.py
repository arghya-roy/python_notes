'''
If-expression if(Condition) else else-expression 

is same as - 

if condition:
   if-expression
else:
   else-expression
'''

a = input("give a ")
b = input("give b ")
print("a is greater than b") if a > b else print("b is greater than a")