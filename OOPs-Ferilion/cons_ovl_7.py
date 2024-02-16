'''Create a class Product with a constructor that can be initialized with either the product's name
and price or just the name (price defaults to 0.0).'''

class Product:

    def __init__(self, name, price = 0.0):
        self.name = name
        self.price = price
# Example usage:
# Creating a Product with name and price
product1 = Product("Laptop", 1200.0)
print(f"Product 1: Name={product1.name}, Price=${product1.price:.2f}")

# Creating a Product with only name (default price to 0.0)
product2 = Product("Mouse")
print(f"Product 2: Name={product2.name}, Price=${product2.price:.2f}")