# way to add items of a list -
list = [1,2,3,4,2]
num = 0
for i in list:
    num = num + i
print(num)

################################################

# using reduce function
from functools import reduce

def add1(x,y):
    return x+y
list1 = [1,2,3,4,2]
num = reduce(add1, list1)  # reduce function at first take x = 1, y = 2, then add it. then take x = 3, and y = 3 then add ..... 

print(num)