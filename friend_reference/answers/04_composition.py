# Practice 04 — Example answer
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
class Market:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def list_items(self):
        for item in self.items:
            print(f'{item.name} — quantity: {item.quantity}, price: {item.price}')
market = Market('Little Market')
market.add_item(Item('Apple', 10, 5))
market.add_item(Item('Iron', 3, 30))
market.list_items()
