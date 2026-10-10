# Practice 07 — Small Market Simulation
#
# Goal:
# Let a customer buy an item through the Market.
# The Market finds the Item, then asks that Item to handle the sale.
#
# Your task is to complete the TODOs. Keep the responsibilities separate:
# - Item manages its own quantity.
# - Market finds items and delegates the sale.
#
# Run with:
#     python market_practice.py


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def sell(self, amount):
        # TODO 1:
        # Return False if amount is zero/negative OR greater than the stock.
        # Otherwise subtract amount from quantity and return True.
        if amount <= 0 or amount > self.quantity or type(amount) != int:
            return
        self.quantity -= amount
        return self.quantity, True

class Market:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def sell_item(self, item_name, amount):
        # TODO 2:
        # Find the item by name, ignoring uppercase/lowercase differences.
        # If found, return the result of item.sell(amount).
        # If not found, return False.
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item.sell(amount)
        return False

    def show_items(self):
        print(f"Items in {self.name}:")
        for item in self.items:
            print(f"{item.name}: {item.quantity} in stock")


market = Market("Little Market")
apple = Item("Apple", 10, 5)
iron = Item("Iron", 3, 30)

market.add_item(apple)
market.add_item(iron)

market.show_items()

print(market.sell_item("apple", 4))  # Expected: True
print(market.sell_item("IRON", 3))   # Expected: True
print(market.sell_item("Gold", 1))   # Expected: False (not in the market)
print(market.sell_item("Apple", 0))  # Expected: False (invalid amount)
print(market.sell_item("Apple", 99)) # Expected: False (not enough stock)

market.show_items()

# Expected final stock:
# Apple: 6 in stock
# Iron: 0 in stock
