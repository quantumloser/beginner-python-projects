name=input("ENTER NAME OF THE ITEM: ")
quantity=int(input('ENTER QUANITITY OF ITEM: ')) 
price=float(input("ENTER THE PRICE OF THE ITEM: "))

cost=quantity*price
if cost>=500:
    discount=cost*0.1
else: 
    discount=0

final_cost=cost-discount


print('THANK YOU, HERE IS THE FINAL BILL: ')
print("ITEM NAME: ", name)
print("QUANTITY OF THE ITEM: ", quantity)
print("PRICE PER ITEM: ", price)
print('DISCOUNT APPLIED: ', discount)
print("TOTAL COST OF THE ITEM: ", final_cost)
