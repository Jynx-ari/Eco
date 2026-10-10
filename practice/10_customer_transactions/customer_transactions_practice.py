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
    pass

    # TODO 2 — Lessons 02 and 09:
    # Write show_balance(self) to print this customer's name and balance,
    # including the shared currency attribute.


class Item:
    # TODO 3 — Lessons 01–03:
    # Write __init__(self, name, quantity, price).
    # Store all three values as instance attributes.
    pass

    # TODO 4 — Lessons 03, 06, and 07:
    # Write sell(self, amount).
    # Return False if amount is not an integer, is <= 0, or exceeds stock.
    # Otherwise subtract amount from quantity and return True.


class Market:
    # TODO 5 — Lessons 02 and 04:
    # Write __init__(self, name).
    # Store the market name, create self.items as an empty list,
    # and create self.sales_history as an empty list.
    # These lists must belong to each Market object, not the class.
    pass

    # TODO 6 — Lessons 04 and 06:
    # Write add_item(self, item) to append an Item object to self.items.

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

    # TODO 8 — Lesson 09:
    # Write show_sales_history(self).
    # Loop through self.sales_history and print useful receipt fields.


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
    pass

    # TODO 10 — Test the rules from Lessons 03 and 08:
    # Try to buy more passes than Alex can afford.
    # Before the failed purchase, record Alex's balance, the chosen item's
    # stock, Alex's transaction-history length, and the market-history length.
    # Confirm that NONE of those values change after the purchase fails.
    #
    # Also test a missing item name and an invalid quantity such as 0.
    # Confirm that failed purchases do not change customer or market state.
