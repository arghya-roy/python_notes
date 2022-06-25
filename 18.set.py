'''
Once a set is created, you can not change any of its items. Although you can add new items or remove previous but updating an already existing item is not possible.
There is no indexing in sets, so accessing an item in order or through a key is not possible, 
although we can ask the program if the specific keyword we are looking for is present in the set by using the “in” keyword or by looping through the set by using a for loop.
Sets are iterable(iterations can be performed using loops)
They are mutable (can be updated by adding or removing entries)
There is no duplication (two same entries do not occur)
Elements of the sets are written in between two curly brackets and are separated with a comma, and in this simple way, we can create a set in Python.
The other way of forming a set is by using a built-in set constructor function.
'''

# set is a list inside a first bracket ([])
# set can also be defined as {}
s = set([1,2,3])
print(s)

l1 = ["l1", "l2", "l3"]
s1 = set(l1)
print(s1)


# Some of the methods you can use with sets include union(), discard(), add(), isdisjoint(), etc., and their functionality is the same as in the sets in mathematics.

s = set()
print(type(s))
s.add(1)
s.add(2)
s.remove(2)
s1 = {4, 6, 1}

print(s.union(s1))

print(s.intersection(s1))

print(s.isdisjoint(s1))