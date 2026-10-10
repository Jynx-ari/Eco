# Practice 09 — Reading Purchase Receipts
#
# Goal:
# Use the dictionary returned by Market.buy_item().
#
# In Practice 08, buy_item() returns either:
# - a dictionary describing a successful purchase, or
# - None when the purchase fails.
#
# Your task is to finish print_receipt() so it can handle both cases.
#
# Run with:
#     python receipt_practice.py


def print_receipt(receipt):
    # TODO 1:
    # If receipt is None, print:
    # Purchase failed.
    # Then stop this function using return.
    #
    # Hint: compare receipt with None.
    if receipt == None:
        return print("Purchase Failed")
    # TODO 2:
    # If a receipt exists, print these details using its dictionary keys:
    # Item: Apple
    # Quantity: 4
    # Total: 20
    # Remaining stock: 6
    #
    # Use receipt["item"], receipt["quantity"],
    # receipt["total_cost"], and receipt["remaining_stock"].
    else:
        print(f"""
        Item: {receipt["item"]}
        Quantity: {receipt["quantity"]}
        Total: {receipt["total_cost"]}
        Remaining Stock: {receipt["remaining_stock"]}""")
        return True

    


# Example receipt, similar to the one returned in Practice 08.
successful_receipt = {
    "success": True,
    "item": "Apple",
    "quantity": 4,
    "total_cost": 20,
    "remaining_stock": 6,
}

failed_receipt = None

print("Successful purchase:")
print_receipt(successful_receipt)

print()

print("Failed purchase:")
print_receipt(failed_receipt)

# Expected output:
# Successful purchase:
# Item: Apple
# Quantity: 4
# Total: 20
# Remaining stock: 6
#
# Failed purchase:
# Purchase failed.
