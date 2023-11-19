# Problem:
# Write an algorithm and a program that first takes today's number,
# then the amount of rain per square meter (kg) for each day of the month
# from the user (there is no need for error checking) and prints
# the following statistical information for that month on the screen.
#
# - Number and percentage of rainy days
# - Average amount of rain per day (kg)


#Algorithm:
# day_count=input()
#
# rainy_day_count=0
# total_rain_amount=0
#
# for day_no in range(1,day_count+1):
#     print(day_no)
#     daily_rain_amount=input()
#
#     total_rain_amount += daily_rain_amount
#     if daily_rain_amount>0:
#         rainy_day_count+=1
#
# print(rainy_day_count, rainy_day_count*100/day_count)
# print(total_rain_amount/day_count)


#Program:
day_count=int(input("What day of the month is today?"))

rainy_day_count=0
total_rain_amount=0

for day_no in range(1,day_count+1):
    daily_rain_amount=float(input(f"Enter the amount of rain for the {day_no}. day(kg):"))

    total_rain_amount += daily_rain_amount
    if daily_rain_amount>0:
        rainy_day_count+=1

print(f"Number of rainy days: {rainy_day_count} and percentage of rainy days: {rainy_day_count*100/day_count:.2f}%")
print(f"Average amount of rain per day: {total_rain_amount/day_count:.2f} kg")
