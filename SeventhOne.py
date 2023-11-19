days=int(input("how many days:"))
total_payment=0
for i in range(days):
    payment=2**i
    total_payment+=payment
    print(payment/100)

print(total_payment/100)

