a=int(input("haftada kaç saat çalışılıyor?"))
normal_hours=40
extra_work_rate=1.5
payment_in_a_hour=53.45
if a<=40:
    wage=a*payment_in_a_hour
else:
    wage=((a-normal_hours)*extra_work_rate*payment_in_a_hour)+a*payment_in_a_hour

print(f"total payment the worker will recieve is:{wage:,.2f}")
