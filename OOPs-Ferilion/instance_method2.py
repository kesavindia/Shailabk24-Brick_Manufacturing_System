'''Write a class ShoppingCart with an instance method add_item(item) that adds the item to the cart.
 Initialize the cart as an empty list in the constructor (__init__).'''

class ShoppingCart:
    def __init__(self):
        self.cart = []
    def add_item(self,item):
        if item is not None:
            self.cart.append(item)
        print(f"Item {item} added in the cart.")
amazon = ShoppingCart()
amazon.add_item("phone")
print(amazon.cart)