'''Modes of opening file in Python:

r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.  - default


w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if 
    there is already some data present in the file, it overwrites it. 
    If the file does not exist then it will create the file then do write.


x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.


a : a stands for append, which means to add something to the end of the file. It does exactly the same. 
   It just adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. 
   It also does not have the permission of reading the file.

t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file data as a string. - default

b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include images, documents, 
    or all other files that require specific software to be read.

+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update our file.

Is it necessary to close a file?
The answer is yes, it is always the best practice to close a file after you are done performing operations on it. However, 
Python runs a garbage collector to clean up the unused objects, but as good programmers, we must not rely on it to close the file. 
Python has a build-in close() function to close a file i.e;
f.close()

'''

# Python has a built-in open() function to open a file.
# open("filename" ,"mode")

# open("myfile.txt")
# The file “myfile.txt” will open in "rt" mode as it is the default mode. But the best practice is to follow the syntax to avoid errors.
# f=open("myfile.txt," "w")

##################################################################################################################################################

# read whole file
file=open("myfile.txt", "rt")
content = file.read()
print(content)
file.close()

##################################################################################################################################################

# read first 5 character of a  file
file=open("myfile.txt", "rt")
content = file.read(5)
print(content)
file.close()   # If you dont close here, after that when you run again content = file.read(5), then it will read next 5 char after first 5 chars.

##################################################################################################################################################

# # overwrite file
# file=open("myfile.txt", "w")
# file.write("suvo is a good boy")
# file.close()

##################################################################################################################################################

# append line to a file
file=open("myfile.txt", "a")
file.write("hiii")
file.close()

##################################################################################################################################################

# create a new file
try:
    file=open("myfile.txt", "x")
    file.close()
except Exception as e:
    print(e)

##################################################################################################################################################

# print each line of a existing file -
file=open("myfile.txt", "rt")
# content = file.read()  # if you do this then file pointer will be empty after read, so have to ignore this
for line in content:
    print(line , end="")

##################################################################################################################################################

# store lines in a list

file=open("myfile.txt","r")
print(file.readlines()) #Returns a list object

##################################################################################################################################################

# read and write (append)

file = open("myfile.txt", "r+")
content = file.read()
print(content)
file.write("\ngood")
content = file.read()
print(content)
file.close()