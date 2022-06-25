'''with open("harry.txt") as file1
   
   is equal to

   file1 = open("harry.txt")
   file1.close()

No need to close when you open this with open block.
'''

with open("harry.txt") as file:
    a = file.readlines()
    print(a)
