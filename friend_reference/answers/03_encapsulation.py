# Practice 03 — Example answer
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.__quantity = quantity
        self.price = price
    def get_quantity(self):
        return self.__quantity
    def restock(self, amount):
        if amount <= 0:
            return False
        self.__quantity += amount
        return True

apple = Item('Apple', 10, 5)
print(apple.get_quantity())
print(apple.restock(5))
print(apple.get_quantity())
# Uncomment the next line to observe an AttributeError:
# print(apple.__quantity)
