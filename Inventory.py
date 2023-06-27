class Item:
    def __init__(self, name, description, quantity=1):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return self.name


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name].quantity += quantity
        else:
            item.quantity = quantity
            self.items[item.name] = item
        print(f"Added {quantity} {item.name}(s) to the inventory.")

    def remove_item(self, item, quantity=1):
        if item.name in self.items:
            if self.items[item.name].quantity >= quantity:
                self.items[item.name].quantity -= quantity
                print(f"Removed {quantity} {item.name}(s) from the inventory.")
            else:
                print("Not enough quantity in the inventory.")
            if self.items[item.name].quantity == 0:
                self.items.pop(item.name)
        else:
            print("Item not found in the inventory.")

    def check_inventory(self):
        print("\n\nInventory:")
        for item in self.items.values():
            print(f"{item.name}: {item.quantity}")
            print(f"Description: {item.description}")

    def pick_up_item(self, item, quantity=1):
        self.add_item(item, quantity)
        print(f"Picked up {quantity} {item.name}(s).")

    def get_inv(self):
        arr = []
        for i in self.items:
            arr.append(i.name)
        return arr

