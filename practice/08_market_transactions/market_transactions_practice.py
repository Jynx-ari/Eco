# Practice 08 — Market Transactions
#
# Goal:
# Let a customer buy an item if they have enough money and receive a receipt.
#
# This builds on Practice 07:
# - Item manages its own stock.
# - Market finds the item and coordinates the purchase.
# - A purchase succeeds only if stock and customer balance are sufficient.
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
    def __init__(self, name, customer_balance):
        self.name = name
        self.customer_balance = customer_balance
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def buy_item(self, item_name, amount):
        # Find the item without worrying about capitalization.
        # Check stock and affordability before changing anything.
        # Return None if the purchase fails.
        for item in self.items:
            if item.name.lower() == item_name.lower():
                # Validate the amount before calculating the cost.
                if type(amount) != int or amount <= 0 or amount > item.quantity:
                    return None

                total_cost = amount * item.price

                # Do not take stock or money if the customer cannot pay.
                if total_cost > self.customer_balance:
                    return None

                # The checks passed, so complete the purchase.
                if not item.sell(amount):
                    return None

                self.customer_balance -= total_cost

                return {
                    "success": True,
                    "item": item.name,
                    "quantity": amount,
                    "total_cost": total_cost,
                    "remaining_stock": item.quantity,
                    "remaining_balance": self.customer_balance,
                }

        return None

    def show_items(self):
        print(f"Items in {self.name}:")
        for item in self.items:
            print(f"{item.name}: {item.quantity} in stock")


if __name__ == "__main__":
    market = Market("Little Market", 50)
    apple = Item("Apple", 10, 5)
    iron = Item("Iron", 3, 30)

    market.add_item(apple)
    market.add_item(iron)

    print("Buying 4 apples (cost: 20):")
    print(market.buy_item("apple", 4))

    print()
    print("Trying to buy 2 iron (cost: 60, but only 30 remains):")
    print(market.buy_item("IRON", 2))  # None; no money or stock is changed

    print()
    print("Buying 1 iron (cost: 30):")
    print(market.buy_item("IRON", 1))

    print()
    print("Buying missing gold:")
    print(market.buy_item("Gold", 1))  # None

    print()
    print("Trying to buy too many apples:")
    print(market.buy_item("Apple", 99))  # None

    print(f"Customer balance: {market.customer_balance}")
    market.show_items()

    # Expected final balance: 0
    # Expected final stock:
    # Apple: 6 in stock
    # Iron: 2 in stock
