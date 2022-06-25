list1 = ['harry', 'ram', 'Aakash', 'shyam', 5, 4.85]

                        # Lists in Python
'''

[]                                             # list with no member, empty list
[1, 2, 3]                                    # list of integers 
[1, 2.5, 3.7, 9]                           # list of numbers (integers and floating point)
['a', 'b', 'c']                               # lisst of characters
['a', 1, 'b', 3.5, 'zero']                # list of mixed value types
['One', 'Two', 'Three']               # list of strings 
'''

# List Methods :

l1=[1,8,4,3,15,20,25,89,65]       #l1 is a list
print(l1)
l1.sort()
print(l1)      #l1 after sorting
l1.reverse()
print(l1)      #l1 after reversing all elements


list1=[1,2,3,6,5,4]     #list1 is a list
print(list1)
list1.append(7)    # This will add 7 in the last of list 
print(list1)
list1.insert(3,8)    # This will add 8 at 3 index in list
print(list1)
list1.remove(1)    #This will remove 1 from the list 
print(list1)
list1.pop(2)          #This will delete and return index 2 value.


list2=[1,2,3,6,5,4]
seq = list2[0:2]
print(seq)

seq = list2[0:2:3] # include every 3rd element, skip 2 element in between
print(seq)

seq = list2[::3] # include every 3rd element from entire list, skip 2 element in between
print(seq)

l4=['One', 'Two', 'Three'] 
print(l4)
l4.sort()
print(l4)      #l1 after sorting with 1st word
l4.reverse()
print(l4)  
l4.append("suvo")    # This will add 7 in the last of list 
print(l4)
l4.insert(3,8)    # This will add 8 at 3 index in list
print(l4)
l4.remove("One")    #This will remove 1 from the list 
print(l4)
l4.pop(2)          #This will delete and return index 2 value.
