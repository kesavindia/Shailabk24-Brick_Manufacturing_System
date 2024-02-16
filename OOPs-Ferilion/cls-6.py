'''Implement an instance method add_item()
 in a class called ShoppingCart that adds an item
 to the cart and prints the item name using self.'''
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,item_name):
        self.items.append(item_name)
        print(f"{item_name} added to the cart")
jam = ShoppingCart()
soap = ShoppingCart()
jam.add_item("kissan")
soap.add_item("hamam")
jam.add_item("patanjali")
print(soap.items)
print(jam.items)