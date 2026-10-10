# Lesson 10 — The CAET Study Market
#
# Goal:
# Review the ideas from Lessons 01–09 by rebuilding a small market that
# will eventually become part of a College Entrance Exam practice system.
#
# Project idea:
# Customers can buy study passes from a market. In later lessons, the
# project will grow to include practice questions for:
# - Mathematics
# - English
# - Science
# - Mental Ability
#
# For now, a study pass is simply an Item. Do not build the quiz system yet.
# Lesson 11 will introduce Question objects and begin connecting questions
# to this project.
#
# Revisit these ideas as you work:
# - Lessons 01–02: classes, objects, __init__, self, attributes, and methods
# - Lesson 03: validate data before changing it
# - Lesson 04: Market contains Item objects (composition)
# - Lesson 05: ordinary classes are enough here; no dataclass is required
# - Lesson 06: Market asks an Item object to perform its own sale
# - Lesson 07: find an item by name and handle missing items
# - Lesson 08: validate purchases and return a receipt dictionary
# - Lesson 09: read receipts and loop through saved transaction history
#
# Lesson rule:
# Rewrite the ideas here for practice. Do not import code from earlier
# lesson folders. Keep any code reuse inside this Lesson 10 folder.
# Do not add a Question class yet; that belongs to Lesson 11.


class Customer:
    # TODO 1 — Lessons 01–02:
    # Add a class attribute: currency = "PHP".
    #
    # Write __init__(self, name, balance).
    # Store name and balance on this customer using self.
    # Create self.transaction_history as a NEW empty list for each customer.
    currency = "PHP"
    currency_symbol = "P"

    def __init__(self, name, balance: int):
        self.name = name
        self.balance: int = balance
        self.transaction_history = []

    # TODO 2 — Lessons 02 and 09:
    # Write show_balance(self) to print this customer's name and balance,
    # including the shared currency attribute.
    def show_balance(self, show_details=True):
        if show_details:
            print(f"\n=== {self.name}'s Balance ===")
            print(f"Currency: {self.currency}")
            print(f"Balance: {self.currency_symbol}{self.balance}")
            print("===========================")
        return self.balance


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def sell(self, amount):
       
        if amount <= 0 or amount > self.quantity or type(amount) != int:
            return False
        self.quantity -= amount
        return True


class Market:
    # TODO 5 — Lessons 02 and 04:
    # Write __init__(self, name).
    # Store the market name, create self.items as an empty list,
    # and create self.sales_history as an empty list.
    # These lists must belong to each Market object, not the class.
    pass
    def __init__(self, name):
        self.name = name
        self.items = []
        self.sales_history = []
    # TODO 6 — Lessons 04 and 06:
    # Write add_item(self, item) to append an Item object to self.items.

    def add_item(self, item):
        self.items.append(item)

    # TODO 7 — Lessons 06–08:
    # Write buy_item(self, customer, item_name, amount).
    #
    # 1. Find the item by name, ignoring capitalization.
    # 2. If the item is missing, return None.
    # 3. Calculate total_cost = amount * item.price.
    # 4. Reject invalid quantities and purchases the customer cannot afford.
    # 5. Ask the Item object to sell the amount. If it fails, return None.
    # 6. Only after validation and a successful sale, subtract total_cost
    #    from customer.balance.
    # 7. Create and return a receipt dictionary with:
    #    success, customer, item, quantity, total_cost,
    #    remaining_stock, remaining_balance.
    # 8. Append that receipt to BOTH customer.transaction_history
    #    and market.sales_history.
    #
    # Remember Lesson 03 / 08: check conditions before changing state.
    # For this lesson, buying a study pass is still an ordinary purchase.
    # We will add quiz behavior in later lessons.

    def buy_item(self, customer, item_name, amount):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                if type(amount) != int or amount <= 0 or amount > item.quantity:
                    return None

                total_cost = amount * item.price
                if total_cost > customer.balance:
                    return None

                # Complete the purchase only after all checks pass.
                if not item.sell(amount):
                    return None

                customer.balance -= total_cost

                receipt = {
                    "customer": customer.name,
                    "success": True,
                    "item": item.name,
                    "quantity": amount,
                    "total_cost": total_cost,
                    "remaining_stock": item.quantity,
                    "remaining_balance": customer.balance,
                }

                # Only successful purchases belong in the history.
                customer.transaction_history.append(receipt)
                self.sales_history.append(receipt)
                return receipt

        return None

    # TODO 8 — Lesson 09:
    # Write show_sales_history(self).
    # Loop through self.sales_history and print useful receipt fields.
    def show_sales_history(self):
        print(f"\n=== {self.name} Sales History ===")
        if not self.sales_history:
            print("No sales recorded yet.")
            return

        for index, sales in enumerate(self.sales_history, start=1):
            print(f"\nSale #{index}")
            print(f"Customer: {sales['customer']}")
            print(f"Item: {sales['item']}")
            print(f"Quantity: {sales['quantity']}")
            print(f"Total Cost: P{sales['total_cost']}")
            print(f"Remaining Stock: {sales['remaining_stock']}")
            print(f"Balance Left: P{sales['remaining_balance']}")
        print("==============================")


def print_receipt(receipt):
    if receipt is None:
        print("\nPurchase failed. Please check the quantity, stock, or balance.")
        return

    print("\n==============================")
    print("PURCHASE RECEIPT")
    print("==============================")
    print(f"Customer: {receipt['customer']}")
    print(f"Item: {receipt['item']}")
    print(f"Quantity: {receipt['quantity']}")
    print(f"Total Cost: P{receipt['total_cost']}")
    print(f"Remaining Stock: {receipt['remaining_stock']}")
    print(f"Remaining Balance: P{receipt['remaining_balance']}")
    print("==============================")


def print_transaction_history(history):
    print(f"\n=== {history[0]['customer']}'s Transaction History ===")
    for index, entry in enumerate(history, start=1):
        print(f"\nTransaction #{index}")
        print(f"Item: {entry['item']}")
        print(f"Quantity: {entry['quantity']}")
        print(f"Total Cost: P{entry['total_cost']}")
        print(f"Remaining Balance: P{entry['remaining_balance']}")
    print("=======================================")


if __name__ == "__main__":
    # TODO 9 — Review Lessons 01–09:
    # Create Alex with a balance of 100.
    # Create a market named "CAET Study Market".
    #
    # Add these Items to the market:
    # - "Math Practice Pass": quantity 10, price 20
    # - "English Practice Pass": quantity 10, price 20
    # - "Science Practice Pass": quantity 10, price 20
    # - "Mental Ability Practice Pass": quantity 10, price 20
    #
    # Buy one Math Practice Pass for Alex and print the returned receipt.
    # Show Alex's balance and personal transaction history.
    # Show the market's sales history.
    market = Market("CAET Study Market")
    alex = Customer("Alex", 100)
    math_pass = Item("Math Practice Pass", 10, 20)
    english_pass = Item("English Practice Pass", 10, 20)
    science_pass = Item("Science Practice Pass", 10, 20)
    mental_ability_pass = Item("Mental Ability Practice Pass", 10, 20)
    market.add_item(math_pass)
    market.add_item(english_pass)
    market.add_item(science_pass)
    market.add_item(mental_ability_pass)
    receipt = market.buy_item(alex, "Math Practice Pass", 1)
    print_receipt(receipt)
    alex.show_balance()
    print_transaction_history(alex.transaction_history)
    market.show_sales_history()

    # TODO 10 — Test the rules from Lessons 03 and 08:
    # Try to buy more passes than Alex can afford.
    # Before the failed purchase, record Alex's balance, the chosen item's
    # stock, Alex's transaction-history length, and the market-history length.
    # Confirm that NONE of those values change after the purchase fails.
    #
    # Also test a missing item name and an invalid quantity such as 0.
    # Confirm that failed purchases do not change customer or market state.
    
    before_balance = alex.balance
    before_stock = math_pass.quantity
    before_customer_history = len(alex.transaction_history)
    before_market_history = len(market.sales_history)

    error_receipt = market.buy_item(alex, "Math Practice Pass", 10)
    print_receipt(error_receipt)

    if before_balance == alex.balance and before_stock == math_pass.quantity and before_customer_history == len(alex.transaction_history) and before_market_history == len(market.sales_history):
        print("\nFailed purchase was rejected safely. No customer or market state changed.")
    else:
        print("\nUnexpected change after failed purchase.")

    missing_item_receipt = market.buy_item(alex, "History Pass", 1)
    print_receipt(missing_item_receipt)

    invalid_quantity_receipt = market.buy_item(alex, "Math Practice Pass", 0)
    print_receipt(invalid_quantity_receipt)

    alex.show_balance()
    market.show_sales_history()

