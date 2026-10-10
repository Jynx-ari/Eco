# Practice 09 — Reading Purchase Receipts
#
# Goal:
# Print the receipt returned by Market.buy_item(), including the remaining balance.
#
# This file reuses the Item and Market classes from Practice 08.
# It does not define a second copy of those classes.
#
# Run from the repository root:
#     python practice/09_reading_receipts/receipt_practice.py

import importlib.util
from pathlib import Path


def print_receipt(receipt):
    if receipt is None:
        print("Purchase failed.")
        return

    print(f"Item: {receipt['item']}")
    print(f"Quantity: {receipt['quantity']}")
    print(f"Total: {receipt['total_cost']}")
    print(f"Remaining stock: {receipt['remaining_stock']}")
    print(f"Remaining balance: {receipt['remaining_balance']}")


# Load the existing market classes from Practice 08.
practice_folder = Path(__file__).resolve().parents[1]
market_file = practice_folder / "08_market_transactions" / "market_transactions_practice.py"

spec = importlib.util.spec_from_file_location("market_transactions_practice", market_file)
market_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(market_module)

Market = market_module.Market
Item = market_module.Item


if __name__ == "__main__":
    market = Market("Little Market", 50)
    market.add_item(Item("Apple", 10, 5))
    market.add_item(Item("Iron", 3, 30))

    print("Successful purchase:")
    receipt = market.buy_item("apple", 4)
    print_receipt(receipt)

    print()
    print("Unaffordable purchase:")
    receipt = market.buy_item("iron", 2)
    print_receipt(receipt)
