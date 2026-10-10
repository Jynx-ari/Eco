# Practice 06 — Object Collaboration
# Goal: learn how one object can ask another object to do something through a method.
#
# Run with: python item_practice.py

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount):
        if amount <= 0:
            return False
        self.quantity += amount
        return True


class Market:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    # TODO 1:
    # Add a method called restock_item(self, item_name, amount).
    def restock_item(self, item_name, amount):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item.restock(amount)
        return False
    # It should:
    # - loop through self.items
    # - find the item whose name matches item_name (case-insensitive)
    # - call that item's restock(amount) method
    # - return True if the item was found and restocking succeeded
    # - return False if the item was not found or restocking failed
    
    # Hint: the Item already knows how to restock itself.
    # The Market only needs to find the right Item and ask it to do the work.

    # TODO 2:
    # Add a method called show_items(self).
    # It should print each item's name and quantity.
    # Hint: loop through self.items.
    def show_items(self):
        for item in self.items:
            print(item.name.lower(), item.quantity)

# Starter data — use these objects to test your methods.
market = Market("Little Market")
apple = Item("Apple", 10, 5)
iron = Item("Iron", 3, 30)

market.add_item(apple)
market.add_item(iron)

# TODO 3: Uncomment these tests after implementing the methods.
market.show_items()
print(market.restock_item("apple", 5))  # Expected: True
print(market.restock_item("IRON", 2))   # Expected: True
print(market.restock_item("Gold", 4))   # Expected: False
print(market.restock_item("Apple", 0))  # Expected: False
market.show_items()
#
# Expected final quantities if all tests run:
# Apple: 15
# Iron: 5
