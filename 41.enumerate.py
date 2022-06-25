# print only which is in even position
########################################################################

l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]
i = 0
for item in l1:
    if i%2 is 0:
        print(f"Jarvis please buy {item}")
    i += 1


########################################################################
# another way-
# enumerate- It picks index with list value, So using this We dont need to use i variable.

l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")