x = 89
def harry():
    x = 20
    print(x)

harry()  # 20
print(x) # 89


# global keyword
y = 89
def harry2():
   global y
   y = 20
   print(y)

harry2()  # 20
print(y) # 89