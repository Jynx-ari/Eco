# Practice 05 — Example answer
from dataclasses import dataclass
@dataclass
class Item:
    name: str
    quantity: int
    price: float
apple = Item('Apple', 10, 5)
iron = Item('Iron', 3, 30)
print(apple)
print(iron)
print(apple.name, apple.quantity, apple.price)
# A regular dataclass is mutable unless you use frozen=True.
