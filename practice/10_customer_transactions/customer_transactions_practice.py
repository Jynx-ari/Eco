# Lesson 10 — Customer Transactions
#
# Goal:
# Model the customer separately from the market.
# The customer owns their money and personal transaction history.
# The market owns its items and sales history.
#
# Rules for this lesson:
# - Write the classes again from scratch; do not import earlier lessons.
# - Keep all Lesson 10 code in this folder.
# - Complete one TODO at a time and run this file after each step.


class Customer:
    # TODO 1:
    # Add a class attribute named currency with the value "PHP".

    # TODO 2:
    # Write __init__(self, name, balance).
    # Store name and balance as instance attributes.
    # Give every customer their own empty transaction_history list.
    pass

    # TODO 3:
    # Write show_balance(self).
    # Print the customer's name and current balance, using the currency.


class Item:
    # TODO 4:
    # Write __init__(self, name, quantity, price).
    # Store these values as instance attributes.
    pass

    # TODO 5:
    # Write sell(self, amount).
    # Return False if amount is not an integer, is <= 0, or exceeds stock.
    # Otherwise subtract amount from quantity and return True.


class Market:
    # TODO 6:
    # Write __init__(self, name).
    # Store the name, create an empty items list, and create an empty
    # sales_history list. These lists belong to this Market object.
    pass

    # TODO 7:
    # Write add_item(self, item) to add an Item object to the market.

    # TODO 8:
    # Write buy_item(self, customer, item_name, amount).
    # Find the item by name, ignoring capitalization.
    # If the item is missing or the amount is invalid, return None.
    # Calculate the total cost before changing any state.
    # If the customer cannot afford it, return None.
    # Ask the Item object to sell the amount; if it fails, return None.
    # Only after all checks pass:
    # - subtract the total cost from the customer's balance
    # - create a receipt dictionary containing:
    #   success, customer, item, quantity, total_cost,
    #   remaining_stock, remaining_balance
    # - append the receipt to both customer.transaction_history
    #   and market.sales_history
    # - return the receipt

    # TODO 9:
    # Write show_sales_history(self) to print the market's saved sales.


if __name__ == "__main__":
    # TODO 10:
    # Create a customer named Alex with 100 PHP.
    # Create a market named "Little Market".
    # Add 10 apples priced at 5 PHP each.
    # Buy 2 apples for Alex and print the returned receipt.
    # Print Alex's remaining balance and transaction history.
    # Print the market's sales history.
    #
    # TODO 11:
    # Try an unaffordable purchase and verify that the customer's balance,
    # item stock, and both histories remain unchanged.
    pass
