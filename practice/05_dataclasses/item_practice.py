# Practice 05 — Dataclasses
# Goal: learn how dataclasses reduce repetitive code when a class mainly stores data.
#
# Read the starter code first, then complete the TODOs.
# Run with: python item_practice.py

from dataclasses import dataclass


# TODO 1:
# Add the @dataclass decorator directly above this class.
# Then remove the __init__ method and keep the three fields.
#
# Hint: write the fields as:
# name: str
# quantity: int
# price: float
@dataclass
class Item:
    name: str
    quantity: int
    price: float


# TODO 2:
# Create two Item objects:
# apple: name="Apple", quantity=10, price=5
# iron: name="Iron", quantity=3, price=30

apple = Item(name="Apple", quantity=10, price=5)
iron = Item(name="Iron", quantity=3, price=30)

# TODO 3:
# Print apple and iron directly.
# Before you change the class, Python prints a generic object representation.
# After you add @dataclass and the fields, the output should show the field names
# and their values, something like:
# Item(name='Apple', quantity=10, price=5)

print(apple)
print(iron)

# TODO 4 (experiment):
# Print apple.name and apple.quantity separately.

print(apple.name)
print(apple.quantity)
print(apple.price)

# Questions to answer in comments:
# 1. Which lines of code did @dataclass let you remove?
# 2. Does @dataclass stop you from changing apple.quantity later?
