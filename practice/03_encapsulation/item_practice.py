# Practice 03 — Encapsulation
# Goal: keep an item's quantity consistent by controlling how it changes.

class Items:
    def __init__(self, itemname, quant, priceval):
        self.__name = itemname
        self.__quantity = quant
        self.__price = priceval

    # TODO 1: Change the quantity attribute to use a double underscore:
    #         self.__quantity
    #
    # TODO 2: Add a method named get_quantity(self) that returns the quantity.
    #
    # TODO 3: Update restock(self, amount) so it:
    #         - rejects amounts <= 0 by returning False
    #         - increases the quantity for valid amounts
    #         - returns True when successful
    #
    # Hint: use self.__quantity inside the class methods.
    def get_quantity(self):
      return self.__quantity
    
    def restock(self, amount: int):
      if amount <= 0:
        return False
      newquant = self.__quantity + amount
      self.__quantity = newquant
      print(f"restocked! +{amount}, now at {newquant}")
      return True

apple = Items("Apple", 10, 5)

# After completing the TODOs, these should work:
print(apple.get_quantity())  # 10
print(apple.restock(5))      # True
print(apple.get_quantity())  # 15
#
# This direct access should no longer work:
print(apple.__quantity)
