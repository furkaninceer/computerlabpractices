title=input("traniee(tr),specialist(s),team leader(te),manager(m):")
year=int(input("working year:"))
day_off=int(input("day_off:"))
employee_of_month=input("employee_of_month yes or no:")
if day_off==0 and employee_of_month=="yes":
    if title=="tr":
        holiday="turkey"
    elif title=="s":
        holiday="Europe"
    elif title=="te":
        holiday="Far East"
    else:
        holiday="America"
    if year<2:
        days=3
    if year<5:
        days=4
    if year<10:
        days=5
    if year<10:
        days=7
    
    print(f"you won holiday package {days}days  in {holiday}")