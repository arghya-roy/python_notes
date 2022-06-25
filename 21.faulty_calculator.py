'''
Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
'''




print("Welcome to faulty Calculator !!")
print("Enter a operator {+,-,*,/}")
operator=input()
operator_list=["+","-","*","/"]
if operator not in operator_list:
    print("Please enter a valid operator !!")
else:
    print("Enter First value :")
    a=int(input())
    print("Enter Second value :")
    b = int(input())

    if operator == '+':
        if a == 56 and b == 9:
            print(77)
        else:
            print(a + b)

    elif operator == "-":
        print(a - b)

    elif operator == '*':
        if a==45 and b==3:
            print(555)
        else:
            print(a * b)

    else:
        if a == 56 and b == 6:
            print(4)
        else:
            print(a / b)