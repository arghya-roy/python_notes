'''
Arithmetic Operators:

Basic mathematical operations such as addition, multiplication, subtraction, division, etc. 
are performed with the help of arithmetic Operations. It contains nearly all operations that we can perform with the help of a calculator. 
Symbols for such operators include *, /, %, -, //, etc. 
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6)
# print("5 ** 3 is ", 5**3)
# print("5 % 5 is ", 5%5)
# print("15 // 6 is ", 15//6)


Assignment Operators:

The assignment operator is used to assign values to a variable. In some cases, we have to assign a variable’s value to another variable, 
in such cases the value of the right operand is assigned to the left operand. One of the basic signs from which we can recognize an assignment operator is 
that it must have an equal-to(=) sign. Some commonly used assignment operators include +=, -=, /=, etc.
# x = 5
# print(x)
# x %=7 
# x = x+7
# print(x)


Comparison Operators:

They are also known as relational operators. They compare the values on either side of the operator and decide the relation among them. 
Commonly used comparison operators include ==, >, < , >=,etc. 
i == 5
i >= 5
i <= 5
i != 5


Logical Operators:

Logical operators perform logical AND, OR and NOT, operations. They are usually used in conditional statements to join multiple conditions. 
AND, OR and NOT keywords are used to perform logical operations.

age = 29
if age < 33 and age > 20:
	print ("Young Man")
else:
	print(" Not Eligible ")


if age < 18 or age > 60:
	print(" Not Eligible to Work ")
else:
	print(" Please forward Your Resume ")



Identity Operations:

Identity operator checks if two operands share the same identity or not, which means that they share the same location in memory or different. 
“is” and “is not” are the keywords used for identity operands.

a = 20
b = 20

if ( a is b ):
   print "Line 1 - a and b have same identity"
else:
   print "Line 1 - a and b do not have same identity"

if ( id(a) == id(b) ):
   print "Line 2 - a and b have same identity"
else:
   print "Line 2 - a and b do not have same identity"

b = 30
if ( a is b ):
   print "Line 3 - a and b have same identity"
else:
   print "Line 3 - a and b do not have same identity"

if ( a is not b ):
   print "Line 4 - a and b do not have same identity"
else:
   print "Line 4 - a and b have same identity"




Membership Operands:

 Membership operand checks if the value or variable is a part of a sequence or not. The sequence could be string, list, tuple, etc. 
 “in” and “not in” are keywords used for membership operands.

list = [3, 3,2, 2,39, 33, 35,32]
print(324 not in list)  # true
 

Bitwise Operand:

Bitwise operands are used to perform bit by bit operation on binary numbers. First, 
we have to change the format of the number from decimal to binary and then compare them using AND, OR, XOR, NOT, etc.
https://byjus.com/jee/basic-logic-gates/

0 - 00
1 - 01
2 - 10
3 - 11

print(0 & 2)  # 0 = 00, 2 = 10, now when we do 0 & 2 then the output will be -
                                                                              0 0
                                                                              1 0
                                                                              ____
                                                                              0 0    = 0
print(0 | 3)  # 0 = 00, 3 = 11, now when we do 0 & 3 then the output will be -
                                                                              0 0
                                                                              1 1
                                                                              ____
                                                                              1 1    = 3


'''

