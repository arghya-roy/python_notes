# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *

n = int(input("Enter the no. of rows : "))
x = int(input("Enter boolian number : "))
x = bool(x)

if x== True:
    for i in range(n+1):
        for j in range(i):
            print("* ",end="")
        print()
else:
    for i in range(n + 1):
        for j in range(n-i):
            print("* ", end="")
        print()

