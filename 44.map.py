# map(): 
'''"A map function executes certain instructions or functionality provided to it on every item of an iterable."
    It applies a function to all item of list, tuple etc'''

# map(function, iterable) 
def multi(a):
    return a*a

# take all item from the list one by one then put that inside multi(a) one by one then return a object. after that have to convert it to a list.
items = [1, 2, 3, 4, 5]
a=list(map(multi, items))  
print(a)


###################################################
# using lambda
items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x*x), items))
print(a)