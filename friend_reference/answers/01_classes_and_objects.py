# Practice 01 — Example answer
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

apple = Item('Apple', 10, 5)
iron = Item('Iron', 3, 30)
for item in (apple, iron):
    print(item.name, item.quantity, item.price)
