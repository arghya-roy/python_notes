'''
There is no limit to the number of conditions that we could use in our program. We can apply as many elif statements as we want, but we can only use one “else” and one “if” statement.
We can use nested if statements, i.e., if statement within an if statement. It is quite helpful in many cases.
Decision statements can be written using logical conditions, which are:
Equal to  ==      --- Same can be used for string and other types also.
Not equal to  !=   --- Same can be used for string and other types also.
Less than    <
Greater than  >
Greater than equal to >=
Less than equal to  <=
'''

var1 = 6
var2 = 56
var3 = int(input())
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")




list1 = [5, 7, 3]
print(15 not in list1)
if 15 not in list1:
    print("No its not in the list")