total_sales=[]
for i in range(10):
    a_lot=7*[0]
    total_sales.append(a_lot)
    week_total=0
    vendor_no=int(input("vendor_no:"))
    for j in range(7):
        sale=int(input("sale:"))
        total_sales[vendor_no-1][j]+=sale
        week_total+=sale
    print(total_sales[vendor_no-1])
    print(week_total)
for a in range(7):
    day_total=0
    for b in range(10):
        day_total+=total_sales[b][a]
    print(day_total)

print(total_sales)