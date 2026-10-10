# Practice 09 — Example answer
def print_receipt(receipt):
    if receipt is None:
        print('Purchase failed.')
        return
    print(f"Item: {receipt['item']}")
    print(f"Quantity: {receipt['quantity']}")
    print(f"Total: {receipt['total_cost']}")
    print(f"Remaining stock: {receipt['remaining_stock']}")
successful_receipt = {'success': True, 'item': 'Apple', 'quantity': 4, 'total_cost': 20, 'remaining_stock': 6}
failed_receipt = None
print('Successful purchase:')
print_receipt(successful_receipt)
print()
print('Failed purchase:')
print_receipt(failed_receipt)
