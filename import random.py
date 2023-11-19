day_count=int(input("day_count"))
the_total_amount_of_rain=0
rainy_day_count=0

for i in range(1,day_count+1):
    the_amount_of_rain=int(input("the_amount_of_rain"))
    the_total_amount_of_rain+=the_amount_of_rain
    if the_amount_of_rain!=0:
        rainy_day_count+=1
        


print(rainy_day_count,rainy_day_count/day_count*100)
print(the_total_amount_of_rain/day_count)




