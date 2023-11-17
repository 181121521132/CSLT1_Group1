purchase_amounts = [4.95, 9.95, 14.95, 19.95, 24.95]

discount_percentage = 60

for amount in purchase_amounts:

    discount_amount = amount * (discount_percentage / 100)

    new_price = amount - discount_amount

    print("Original Price: ",round(amount,2))
    print("Discount Amount: ",round(discount_amount,2))
    print("New Price: ",round(new_price,2))
    print()
