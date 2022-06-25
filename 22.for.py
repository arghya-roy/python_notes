l1 = ['a', 1, 'b', 3.5, 'zero'] 

for v_name in l1:
    print(v_name)

dict1= {"Best Python Course": "CodeWithHarry",
        "Best C Languge Course": "CodeWithHarry",
        "Harry Sir":"Tom Cruise Of Programming"
        }

for key,value in dict1.items():
    print(key, value)     # print key and value both

for items_name in dict1:
    print(items_name)    # print only key


items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:  # convert all value to string and check that if they are number or not, then check its greater than 6 or not.
        print(item)



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


for x in range(2, 6):
  print(x)
