'''
string.endswith(): This function allows the user to check whether a given string ends with a passed argument or not. It returns True or False.

string.count(): This function counts the total no. of occurrences of any character in the string. It takes the character whose occurrence you want to find as an argument.
example - string.count("u")

string.capitalize(): This function capitalizes the first character of any string. It doesn’t take any argument.

string.upper(): It returns the copy of the string converted to the uppercase.

string.lower(): It returns the copy of the string converted to lower case.

string.find(): This function finds any given character or word in the entire string. It returns the index of the first character from that word.

string.replace(“old_word”, “new_word”): This function replaces the old word or character with a new word or character from the entire string.


'''

demo = "Aakash is a good boy" 
print(demo.endswith("boy"))
print(demo.count('o'))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.find("is"))
print(demo.replace("good","nice"))

mystr = "Harry is a good boy"
print(len(mystr))
print(mystr[0:-2])
print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))

