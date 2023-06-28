from time import sleep as s
def Print2(text):
    for char in text:
        print(char,end="",flush = True)
        s(0.01)
    print()


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

    def add_item(self, item, quantity, bool = True):
        if item.name in self.items:
            self.items[item.name].quantity += quantity
        else:
            item.quantity = quantity
            self.items[item.name] = item

        if bool:
            Print2(f"Added {quantity} {item.name}(s) to the inventory.")

    def remove_item(self, item, quantity=1):
        if item.name in self.items:
            if self.items[item.name].quantity >= quantity:
                self.items[item.name].quantity -= quantity
                Print2(f"Removed {quantity} {item.name}(s) from the inventory.")
            else:
                Print2("Not enough quantity in the inventory.")
            if self.items[item.name].quantity == 0:
                self.items.pop(item.name)
        else:
            Print2("Item not found in the inventory.")

    def check_inventory(self):
        Print2("\n\nInventory:")
        for item in self.items.values():
            Print2(f"{item.name}: {item.quantity}")
            Print2(f"Description: {item.description}")

    def pick_up_item(self, item, quantity=1, bool = True):
        self.add_item(item, quantity)
        if bool:
            Print2(f"Picked up {quantity} {item.name}(s).")


