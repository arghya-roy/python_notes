import time

# calculate total time to execute while loop
initial = time.time()
k = 0
while(k<45):
    print("This is harry bhai")
   # time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds")


# calculate total time to execute for loop
initial2 =time.time()
for i in range(45):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds")


# show current licaltime
localtime = time.asctime(time.localtime(time.time()))  # localtime format give the local time and asctime format the local time
print(localtime)   