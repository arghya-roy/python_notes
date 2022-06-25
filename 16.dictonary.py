'''
It is unordered (no sequence is required - data or entries have no order)
It is mutable (values can be changed even after its formation, or new data/information can be added to the already existing dictionary, we can also pop/remove an entry completely)
It is indexed (Dictionary contains key-value pairs, and indexing is done with keys. Also, after the Python 3.7th update, the compiler stores the entries in the order they are created)
No duplication of data (each key is unique; no two keys can have the same name, so there is no chance for a data being overridden)
'''

# Dictionary is nothing but key value pairs
from hashlib import sha3_384


d1 = {}
print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2)
print(d2["Shubham"])
print(d2["Shubham"]["B"])

# for copy if we used d3=d2, then If we did some change inside d3 then same change will happen inside d2. Because in this case d3 just synchronized with d2. 
# To aviod above probem, we use d3 = d2.copy()

d3 = d2.copy()
print(d3)
del d3["Harry"]
d2.update({"Leena":"Toffee"})  # same as d2["Ankit"] = "Junk Food"
print(d2)
print(d2.keys())
print(d2.items())
