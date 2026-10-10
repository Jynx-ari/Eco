# Practice 09 — Reading Purchase Receipts
# TODO 1: Implement print_receipt(receipt).
# TODO 2: If receipt is None, print 'Purchase failed.' and return.
# TODO 3: Otherwise print Item, Quantity, Total, and Remaining stock using dictionary keys.
# TODO 4: Test with the sample successful and failed receipts.
def print_receipt(receipt):
    pass
successful_receipt = {'success': True, 'item': 'Apple', 'quantity': 4, 'total_cost': 20, 'remaining_stock': 6}
failed_receipt = None
print('Successful purchase:')
print_receipt(successful_receipt)
print()
print('Failed purchase:')
print_receipt(failed_receipt)
