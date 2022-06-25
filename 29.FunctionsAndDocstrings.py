def function2(a,b):
    """This will return sum"""  # this line will print when you call docstring of this function, recommended to call dockstring before calling actual function
    sum = a + b
    print("doing sum")
    return sum   

    
print(function2.__doc__)

print(function2(5,7))