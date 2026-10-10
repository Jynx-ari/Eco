# Practice 07 — Example answer
class Item:
    def __init__(self, name, quantity, price):
        self.name, self.quantity, self.price = name, quantity, price
    def sell(self, amount):
        if type(amount) is not int or amount <= 0 or amount > self.quantity:
            return False
        self.quantity -= amount
        return True
class Market:
    def __init__(self, name):
        self.name, self.items = name, []
    def add_item(self, item):
        self.items.append(item)
    def sell_item(self, item_name, amount):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item.sell(amount)
        return False
    def show_items(self):
        print(f'Items in {self.name}:')
        for item in self.items:
            print(f'{item.name}: {item.quantity} in stock')
market = Market('Little Market')
market.add_item(Item('Apple', 10, 5))
market.add_item(Item('Iron', 3, 30))
market.show_items()
print(market.sell_item('apple', 4))
print(market.sell_item('IRON', 3))
print(market.sell_item('Gold', 1))
print(market.sell_item('Apple', 0))
print(market.sell_item('Apple', 99))
market.show_items()
