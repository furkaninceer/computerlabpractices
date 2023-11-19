purchased_in=input("a or b")
if purchased_in=="a":
    first=20000
    second=19000
    third=17500
    forth=16000
    price=int(input("price:"))
    group_code=input("1,2,3,4")
    
    if group_code=="1":
        total_tax=first+600
    elif group_code=="2":
        total_tax=second+600
    elif group_code=="3":
        total_tax=third+600
    elif group_code=="4":
        total_tax=forth+600
else:
    base_price=int(input("base_price"))
    new_price=base_price*(101/100)*(130/100)
    if new_price<=1500:
        new_price*=1.25
    elif new_price>1500 and new_price<=3000 :
        new_price*=1.40
    elif new_price>3000:
        new_price*=1.50
    last_price=new_price*(120/100)*(130/100)

if purchased_in=="a":
    print(total_tax)
    print(total_tax/(total_tax+price))
    print(total_tax+price)
else:
    print(last_price-base_price)
    print((last_price-base_price)/(last_price))
    print(last_price)

