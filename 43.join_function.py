# want to add and between all names then print

lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

for item in lis:
    print(item, "and", end=" ")

print()
##############################################################

# using join function -

lis1 = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]
a = " and ".join(lis1)
print(a, "other wwe superstars")