# Practice 08 — Market Transactions
#
# Goal:
# Extend the market so a customer can buy an item and learn the total cost.
#
# This builds on Practice 07. There are two small TODOs.
#
# Run with:
#     python market_transactions_practice.py


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def sell(self, amount):
        if type(amount) != int or amount <= 0 or amount > self.quantity:
            return False

        self.quantity -= amount
        return True


class Market:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def buy_item(self, item_name, amount):
        # TODO 1:
        # Find the item by name, ignoring capitalization.
        # If it doesn't exist, return None.
        # If the sale fails, return None.
        # If it succeeds, return the total cost (price * amount).
        #
        # Hint:
        # 1. Loop through self.items.
        # 2. Compare item.name.lower() with item_name.lower().
        # 3. Ask the item to sell the amount.
        # 4. Only if that succeeds, calculate and return the total cost.
        # 5. If no matching item exists, return None.
        pass

    def show_items(self):
        print(f"Items in {self.name}:")
        for item in self.items:
            print(f"{item.name}: {item.quantity} in stock")


market = Market("Little Market")
apple = Item("Apple", 10, 5)
iron = Item("Iron", 3, 30)

market.add_item(apple)
market.add_item(iron)

print("Buying 4 apples:")
print(market.buy_item("apple", 4))  # Expected: 20

print("Buying 3 iron:")
print(market.buy_item("IRON", 3))   # Expected: 90

print("Buying missing gold:")
print(market.buy_item("Gold", 1))   # Expected: None

print("Trying to buy too many apples:")
print(market.buy_item("Apple", 99)) # Expected: None

market.show_items()

# Expected final stock:
# Apple: 6 in stock
# Iron: 0 in stock
