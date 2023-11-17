total_cost = 0

while True:
    price = input("Enter the price (or leave blank to finish): ")
    
    if price == "":
        break
    
    total_cost += float(price)

amount_due = round(total_cost / 0.05) * 0.05

print("Total cost: $", total_cost)
print("Amount due (cash payment): $", amount_due)