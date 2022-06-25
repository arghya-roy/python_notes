
'''
Data Types in Python:
Primarily there are the following data types in Python.

Integers (<class 'int'>): Used to store integers
Floating point numbers (<class 'float'>): Used to store decimal or floating-point numbers
Strings (<class 'str'>): Used to store strings
Booleans (<class 'bool'>): Used to store True/False type values
None: None is literal to describe 'Nothing' in Python
'''


'''
Rules for defining a variable in Python:
A variable name can contain alphabets, digits, and underscores (_). For E.g. : demo_xyz = ‘It’s a string variable’
A variable name can only start with an alphabet and underscore.
It can't start with a digit. For example, 5harry is illegal and not allowed.
No white space is allowed to be used inside a variable name.
Also, reserved keywords are not recommended to be used as variable names.
Examples of few valid variable names are harry, _demo, de_mo, etc.
'''

'''
Variable in Python:

abc = "It's a string variable"
_abcnum = 40 # It is an example of int variable
abc123 = 55.854 # It is an example of float variable
print(_abcnum + abc123) # This will give sum of 40 + 55.854
'''


name = input("what is your name?\n")
length = len(name)
print(length)