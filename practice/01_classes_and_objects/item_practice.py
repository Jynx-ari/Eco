import inflect

p = inflect.engine()

def toNum(txt: str):
      try:
        return int(txt)
      except ValueError:
        try:
            return float(txt)
        except ValueError:
            return txt


class Items:
    def __init__(self,itemname, quant, priceval):
      self.price: int | float = priceval
      self.quantity: int = quant
      self.name: str = itemname
    def description(self):
      print(f"""
      Name: {self.name}
      Only {self.quantity} left!
      Current Price: {self.price}
      """)
    def sell(self, amount: int):
      absamount = toNum(amount)
      if type(absamount) == float or type(absamount) == str:
        return False
      if absamount <= 0:
        return False
      if absamount > self.quantity:
          print("Not enough stock!")
          print(f"Only {self.quantity} are available")
          return False
      self.quantity -= absamount
      print(f"Bought {absamount} {p.plural_noun(self.name.lower(), absamount)}")
      print(f"Only {self.quantity} left!")
      return True


print("Creating apple...")
apple = Items("Apple",53, 5)

print("Creating iron...")
iron = Items("Iron", 3, 30)

apple.description()
iron.description()

apple.sell(input("How much apples do you wanna buy?"))