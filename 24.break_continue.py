# break statement exit the loop when condition is matched, and continue statement start the loop again when condition matches.

while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue

# we can use break and continue only inside a loop.