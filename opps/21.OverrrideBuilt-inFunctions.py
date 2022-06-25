# Overrride Built-in Functions -
'''
In Python, we can change the default behavior of the built-in functions. 
For example, we can change or extend the built-in functions such as len(), abs(), or divmod() by redefining them in our class. 
Let’s see the example.

Example

In this example, we will redefine the function len()
'''
class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count * 2

shopping = Shopping(['Shoes', 'dress'], 'Jessa')
print(len(shopping))