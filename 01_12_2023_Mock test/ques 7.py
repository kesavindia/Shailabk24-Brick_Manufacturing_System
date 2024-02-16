#Discount problem

Total_price = int(input("Enter total price: "))
discount = 0

if Total_price >= 100:
    discount += .1 * Total_price
    Final_price = Total_price-discount
elif 50 <= Total_price > 100:
    discount += .05 * Total_price
    Final_price = Total_price - discount
else:
    Final_price = Total_price
print("discount: ",discount)
print("Final price:Rs."+str(Final_price))