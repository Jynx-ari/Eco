# Practice 06 — Example answer
class Item:
    def __init__(self, name, quantity, price):
        self.name, self.quantity, self.price = name, quantity, price
    def restock(self, amount):
        if amount <= 0:
            return False
        self.quantity += amount
        return True
class Market:
    def __init__(self, name):
        self.name, self.items = name, []
    def add_item(self, item):
        self.items.append(item)
    def restock_item(self, item_name, amount):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item.restock(amount)
        return False
    def show_items(self):
        for item in self.items:
            print(f'{item.name}: {item.quantity}')
market = Market('Little Market')
market.add_item(Item('Apple', 10, 5))
market.add_item(Item('Iron', 3, 30))
market.show_items()
print(market.restock_item('apple', 5))
print(market.restock_item('IRON', 2))
print(market.restock_item('Gold', 4))
print(market.restock_item('Apple', 0))
market.show_items()
