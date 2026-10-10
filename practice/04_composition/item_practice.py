# Practice 04 — Composition
# Goal: model one object that contains and uses another object.
#
# In this exercise, a Market contains Items.
# The Market object should manage a collection of item objects.

class Items:
    def __init__(self, itemname, quant, priceval):
        self.name = itemname
        self.quantity = quant
        self.price = priceval


class Market:
    def __init__(self, market_name):
        self.name = market_name
        self.items = []

    # TODO 1: Add an add_item(self, item) method.
    # It should append the given Items object to self.items.
    def add_item(self, item):
        self.items.append(item)
    # TODO 2: Add a list_items(self) method.
    # It should print each item's name, quantity, and price.
    # Hint: loop through self.items.
    def list_items(self):
        for item in self.items:
            print(f"{item.name} — quantity: {item.quantity}, price: {item.price}")


market = Market("Little Market")
apple = Items("Apple", 10, 5)
iron = Items("Iron", 3, 30)

# After completing the TODOs, these should work:
market.add_item(apple)
market.add_item(iron)
market.list_items()



# Expected information to display:
# Apple — quantity: 10, price: 5
# Iron — quantity: 3, price: 30
