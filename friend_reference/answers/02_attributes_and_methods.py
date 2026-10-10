# Practice 02 — Example answer
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def change_price(self, new_price):
        if new_price < 0:
            return False
        self.price = new_price
        return True
    def total_value(self):
        return self.quantity * self.price
    def restock(self, amount):
        if amount <= 0:
            return False
        self.quantity += amount
        return True

apple = Item('Apple', 10, 5)
print(apple.change_price(7))
print(apple.total_value())
print(apple.restock(20))
print(apple.quantity)
