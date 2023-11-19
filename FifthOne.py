years=int(input("how many years?"))
in_a_year=0
total_rainfall=0
for i in range(years):
    for i in range(12):
        rainfall=int(input("rainfall_in_a_month:"))
        in_a_year+=rainfall
    total_rainfall+=in_a_year
print(12*years)
print(total_rainfall)
print(total_rainfall/12*years)