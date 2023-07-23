price=[5,3,71,3,4,5,9]
buy=price[0]
sell=0
profit=0
for i in range(1,len(price)):
    sell=price[i]
    profit=max(profit,(sell-buy))
    buy=min(buy,price[i])
if profit == 0:
    print("0")
else:
    print(profit)
