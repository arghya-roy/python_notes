# https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
# https://www.educative.io/answers/list-vs-tuple-vs-set-vs-dictionary-in-python

# Various ways to create a list
list1=[1,4,"Gitam",6,"college"]
list2=[]  # creates an empty list
list3=list((1,2,3))
print(list1)
print(list2)
print(list3)

# Various ways to create a tuple
tuple1=(1,2,"college",9)
tuple2=() # creates an empty tuple
tuple3=tuple((1,3,5,9,"hello"))
print(tuple1)
print(tuple2)
print(tuple3)

# How to create a set
set1={1,2,3,4,5,"hello","tup"}
set2={(1,8,"python",7)}
print(set1)
print(set2)

# How to create a dictionary
dict1={"key1":"value1","key2":"value2"}
dict2={}   # empty dictionary
dict3=dict({1:"apple",2:"cherry",3:"strawberry"})
print(dict1)
print(dict2)
print(dict3)