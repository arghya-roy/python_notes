def function1(a, b):
    sum = a + b
    print(sum)

function1(5,6) # When you do function1(5,6) then it will give 11
print()
print(function1(5,6)) # but when you do print(function1(5,6)) then at first it will give 11 after that it will give none, means the function returns none value. So 
                        # to avoid this we use use return sum, instead of print(sum).


print()    
def function2(a,b):
    sum = a + b
    return sum   
print(function2(5,6))

