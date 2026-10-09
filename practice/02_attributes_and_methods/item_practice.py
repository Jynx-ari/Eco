class Items:
    def __init__(self, itemname, quant, priceval):
        self.name = itemname
        self.quantity = quant
        self.price = priceval
    def changePrice(self, newprice: int):
      if newprice < 0:
          print("Price cannot be negative!")
          return self.price
  
      self.price = newprice
      return self.price
      
    def totalVal(self):
      value: int = self.quantity * self.price
      return value
    def restock(self, amount: int):
      if amount <= 0:
        return False
      newquant = self.quantity + amount
      self.quantity = newquant
      print(f"restocked! +{amount}, now at {newquant}")
      return True

      
apple = Items("Apple", 10, 5)

print(apple.name)
print(apple.price)

print(apple.changePrice(7))

print(apple.quantity)

print(apple.totalVal())

print(apple.restock(20))
