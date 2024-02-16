'''28.	Simple Inventory System:
Build a basic inventory management system where users can add, remove, and view items in their
inventory. Utilize loops to handle user interactions and keep the program running until the user
decides to exit.'''
class InventorySystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"{quantity} {item}(s) added to the inventory.")

    def remove_item(self, item, quantity):
        if item in self.inventory:
            if quantity >= self.inventory[item]:
                del self.inventory[item]
                print(f"All {item}(s) removed from the inventory.")
            else:
                self.inventory[item] -= quantity
                print(f"{quantity} {item}(s) removed from the inventory.")
        else:
            print(f"{item} not found in the inventory.")

    def view_inventory(self):
        print("\nCurrent Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
        print()

# Create instances for Amazon and FlipKart
Amazon = InventorySystem()
FlipKart = InventorySystem()

# Choose between Amazon and FlipKart
while True:
    print("\nChoose an inventory system:")
    print("1. Amazon")
    print("2. FlipKart")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        current_inventory_system = Amazon
        print("You've selected Amazon Inventory System.")
        break
    elif choice == "2":
        current_inventory_system = FlipKart
        print("You've selected FlipKart Inventory System.")
        break
    elif choice == "3":
        print("Exiting. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Main loop for the selected inventory system
while True:
    print("\nOptions:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Exit")

    action_choice = input("Enter your choice (1-4): ")

    if action_choice == "1":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity to add: "))
        current_inventory_system.add_item(item, quantity)

    elif action_choice == "2":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity to remove: "))
        current_inventory_system.remove_item(item, quantity)

    elif action_choice == "3":
        current_inventory_system.view_inventory()

    elif action_choice == "4":
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
print(Amazon.inventory)
print(FlipKart.inventory)
