purchase = float(input("Enter the amount of a purchase: "))

stateSalesTax = 0.05 * purchase
countrySalesTax = 0.025 * purchase

totalSalesTax = float(stateSalesTax) + float(countrySalesTax)
totalSale = float(purchase) + float(totalSalesTax)
print("purchase: $", format(purchase, '.2f'))
print("State sales tax: $", format(stateSalesTax, '.2f'))
print("Country sales tax: $", format(countrySalesTax, '.2f'))
print("Total sales tax: $", format(totalSalesTax, '.2f'))
print("Total sale: $" + format(totalSale, ".2f"))