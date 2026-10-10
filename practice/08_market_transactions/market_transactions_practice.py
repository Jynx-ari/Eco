# Practice 08 — Market Transactions
#
# Goal:
# Let a customer buy an item and receive a purchase receipt.
#
# This builds on Practice 07:
# - Item manages its own stock.
# - Market finds the item and delegates the sale to Item.
# - A successful purchase returns a receipt dictionary.
# - A failed purchase returns None.
#
# Run with:
#     python practice/08_market_transactions/market_transactions_practice.py


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
        # Find the item without worrying about capitalization.
        # Return None if the item is missing or the sale fails.
        # Otherwise, return a dictionary describing the purchase.
        for item in self.items:
            if item.name.lower() == item_name.lower():
                if not item.sell(amount):
                    return None

                return {
                    "success": True,
                    "item": item.name,
                    "quantity": amount,
                    "total_cost": amount * item.price,
                    "remaining_stock": item.quantity,
                }

        return None

    def show_items(self):
        print(f"Items in {self.name}:")
        for item in self.items:
            print(f"{item.name}: {item.quantity} in stock")


if __name__ == "__main__":
    market = Market("Little Market")
    apple = Item("Apple", 10, 5)
    iron = Item("Iron", 3, 30)

    market.add_item(apple)
    market.add_item(iron)

    print("Buying 4 apples:")
    print(market.buy_item("apple", 4))  # Receipt: total_cost is 20

    print("Buying 3 iron:")
    print(market.buy_item("IRON", 3))   # Receipt: total_cost is 90

    print("Buying missing gold:")
    print(market.buy_item("Gold", 1))   # None

    print("Trying to buy too many apples:")
    print(market.buy_item("Apple", 99)) # None

    market.show_items()

    # Expected final stock:
    # Apple: 6 in stock
    # Iron: 0 in stock
