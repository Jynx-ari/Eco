# Practice 02 — Attributes and Methods
# TODO 1: Add change_price(new_price); reject negative prices.
# TODO 2: Add total_value() returning quantity * price.
# TODO 3: Add restock(amount); reject amount <= 0 and return True/False.
# TODO 4: Test changing price, calculating value, and restocking.
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
