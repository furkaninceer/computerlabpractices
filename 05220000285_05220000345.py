INDUSTRY_SINGLE_TIME=305.3828 
INDUSTRY_DAY_UNIT=309.1833
INDUSTRY_PEAK_UNIT=490.9037
INDUSTRY_NIGHT_UNIT=162.5171 
INDUSTRY_DISTRIBUTION=64.7998
INDUSTRY_ECT=0.01
INDUSTRY_VAT=0.20


PUBLIC_AND_PRIVATE_LOW_SINGLE_TIME=191.2220 
PUBLIC_AND_PRIVATE_DAY_UNIT=285.8616
PUBLIC_AND_PRIVATE_PEAK_UNIT=458.8843
PUBLIC_AND_PRIVATE_NIGHT_UNIT=148.1941
PUBLIC_AND_PRIVATE_DISTRIBUTION=87.8175
PUBLIC_AND_PRIVATE_STAGE_LIMIT = 30


PUBLIC_AND_PRIVATE_HIGH_SINGLE_TIME=282.8414
PUBLIC_AND_PRIVATE_ECT=0.05
PUBLIC_AND_PRIVATE_VAT=0.20


RESIDENTIAL_LOW_SINGLE_TIME=48.2187    
RESIDENTIAL_DAY_UNIT=115.7700
RESIDENTIAL_PEAK_UNIT=208.3645
RESIDENTIAL_NIGHT_UNIT=41.7225
RESIDENTIAL_DISTRIBUTION=85.8883


RESIDENTIAL_HIGH_SINGLE_TIME=113.2271   

RESIDENTIAL_FAMILY_SINGLE_TIME=6.1590 
RESIDENTIAL_FAMILY_DISTRIBUTION=58.2521
RESIDENTIAL_ECT=0.05
RESIDENTIAL_VAT=0.10
RESIDENTIAL_STAGE_LIMIT = 8


AGRICULTURAL_SINGLE_TIME=165.3096    
AGRICULTURAL_DAY_UNIT=170.4822
AGRICULTURAL_PEAK_UNIT=280.0325
AGRICULTURAL_NIGHT_UNIT=77.1882
AGRICULTURAL_DISTRIBUTION=72.1579
AGRICULTURAL_ECT=0.05
AGRICULTURAL_VAT=0.10

MARTYR_FAMILY_SINGLE_TIME=6.1590 
MARTYR_FAMILY_DISTRIBUTION=58.2521
MARTYR_FAMILY_ECT=0.05
MARTYR_FAMILY_VAT=0.10

LIGHTING_SINGLE_TIME=259.5835  
LIGHTING_DISTRIBUTION=84.1099
LIGHTING_ECT=0.05
LIGHTING_VAT=0.20

martyr_family_consumer_count=0
industrial_consumer_count = 0
residential_consumer_count = 0
public_and_private_consumer_count = 0
agricultural_consumer_count = 0
lighting_consumer_count = 0
not_residential_count = 0


martyr_family_usage_total=0
industrial_usage_total = 0
residential_usage_total = 0
public_and_private_usage_total = 0
agricultural_usage_total = 0
lighting_usage_total = 0

public_and_private_single_tariff_count = 0
public_and_private_multi_tariff_count = 0

highest_residential_usage = 0

not_residential_highest_usage = 0


exceeding_industry_consumer_count = 0 #Those who use more than 10000 kWh or their bill is more than 100000TL
exceeding_industry_consumer_bill_count=0

who_made_a_loss_count=0
not_martyr_family_and_not_lighting_multi=0

total_transferred_to_the_municipality=0
total_transferred_to_the_state=0
total_transferred_to_the_GDZ_corporation=0

def larger_than_zero_and_equal_or_greater_than_the_previous_daytime_period_meter_value(prev,curr):
    prev=int(input(f"{prev}:"))
    if prev<0:
        prev=int(input(f"try again"))
        
    curr=int(input(f"{curr}:"))
    if curr<prev:
        curr=int(input(f"try again"))
    return prev,curr

def zero_or_greater_than_zero(yearly):
    yearly=int(input(f"{yearly}:"))
    if yearly<0:
        yearly=int(input(f"try again"))
    return yearly

def greater_than_zero(days):
    days=int(input(f"{days}:"))
    if days<=0:
        days=int(input(f"try again"))
    return days
    
    




profit_loss_situation = ""
martyr_family = "N"
while True:
    consumer_no = int(input("consumer_no:"))
    if consumer_no==0:
        break
    consumer_type_code = input("consumer_type_code: R,r,I,i,L,l,P,p,A,a")
    previous_day_value="previous_day_value"
    current_day_value="current_day_value"
    previous_peak_value="previous_peak_value"
    current_peak_value="current_peak_value"
    previous_night_value="previous_night_value"
    current_night_value="current_night_value"
    consumption_yearly="consumption_yearly"
    days_between_reading="days_between_reading"
    previous_day_value,current_day_value=larger_than_zero_and_equal_or_greater_than_the_previous_daytime_period_meter_value(previous_day_value,current_day_value)
    previous_peak_value,current_peak_value=larger_than_zero_and_equal_or_greater_than_the_previous_daytime_period_meter_value(previous_peak_value,current_peak_value)
    previous_night_value,current_night_value=larger_than_zero_and_equal_or_greater_than_the_previous_daytime_period_meter_value(previous_night_value,current_night_value)
    consumption_yearly=zero_or_greater_than_zero(consumption_yearly)
    days_between_reading=greater_than_zero(days_between_reading)
    


    night_consumption = current_night_value - previous_night_value
    day_consumption = current_day_value - previous_day_value
    peak_consumption = current_peak_value - previous_peak_value

    total_consumption = night_consumption + day_consumption + peak_consumption
    daily_consumption = total_consumption/days_between_reading

    public_and_private_day = day_consumption*PUBLIC_AND_PRIVATE_DAY_UNIT
    public_and_private_peak = peak_consumption*PUBLIC_AND_PRIVATE_PEAK_UNIT
    public_and_private_night = night_consumption*PUBLIC_AND_PRIVATE_NIGHT_UNIT
    public_and_private_multi = public_and_private_day+public_and_private_peak+public_and_private_night

    industry_day = day_consumption*INDUSTRY_DAY_UNIT
    industry_peak = peak_consumption*INDUSTRY_PEAK_UNIT
    industry_night = night_consumption*INDUSTRY_NIGHT_UNIT
    industry_multi = industry_day+industry_peak+industry_night

    agricultural_day = day_consumption*AGRICULTURAL_DAY_UNIT
    agricultural_peak = peak_consumption*AGRICULTURAL_PEAK_UNIT
    agricultural_night = night_consumption*AGRICULTURAL_NIGHT_UNIT
    agricultural_multi = agricultural_day+agricultural_peak+agricultural_night

    residential_day = day_consumption*RESIDENTIAL_DAY_UNIT
    residential_peak = peak_consumption*RESIDENTIAL_PEAK_UNIT
    residential_night = night_consumption*RESIDENTIAL_NIGHT_UNIT
    residential_multi = residential_day+residential_peak+residential_night

    preferred_tariff = input("preferred_tariff S,s,M,m")
    single_tariff = (preferred_tariff == "S" or preferred_tariff == "s")
    multi_tariff = (preferred_tariff == "M" or preferred_tariff == "m")
    residential = (consumer_type_code == "R" or consumer_type_code == "r")
    industry = (consumer_type_code == "I" or consumer_type_code == "i")
    lighting = (consumer_type_code == "L" or consumer_type_code == "l")
    public_and_private = (consumer_type_code == "P" or consumer_type_code == "p")
    agricultural = (consumer_type_code == "A" or consumer_type_code == "a")

    

    if consumption_yearly>1000:
        free_consumer="free consumer"
    else:
        free_consumer="not free consumer"


    if residential:
        residential_consumer_count += 1
        residential_usage_total += total_consumption

        if total_consumption >= highest_residential_usage:
            highest_residential_usage = total_consumption
            highest_residential_consumer_no = consumer_no
            highest_residential_consumer_daily = total_consumption/days_between_reading

        martyr_family = input("martyr family Y,y,N,n:")
    


    if  (martyr_family == "N" or martyr_family == "n") and (not lighting):

        if multi_tariff:
            not_martyr_family_and_not_lighting_multi+=1


        if public_and_private:
            consumer_type_code="Public and Private Services Sector and Other"
            single_tariff_bill = (total_consumption*PUBLIC_AND_PRIVATE_LOW_SINGLE_TIME*(1+PUBLIC_AND_PRIVATE_ECT)+PUBLIC_AND_PRIVATE_DISTRIBUTION*total_consumption)*(1+PUBLIC_AND_PRIVATE_VAT)
            multi_tariff_bill = (public_and_private_multi*(1+PUBLIC_AND_PRIVATE_ECT)+PUBLIC_AND_PRIVATE_DISTRIBUTION*total_consumption)*(1+PUBLIC_AND_PRIVATE_VAT)
            if single_tariff:
                public_and_private_single_tariff_count += 1
                if daily_consumption <= PUBLIC_AND_PRIVATE_STAGE_LIMIT:
                    bill = single_tariff_bill 
                    transferred_to_the_municipality = total_consumption*PUBLIC_AND_PRIVATE_LOW_SINGLE_TIME*PUBLIC_AND_PRIVATE_ECT
                    transferred_to_the_state = single_tariff_bill/(1+PUBLIC_AND_PRIVATE_VAT)*PUBLIC_AND_PRIVATE_VAT

                elif daily_consumption > PUBLIC_AND_PRIVATE_STAGE_LIMIT:
                    low_consumption = PUBLIC_AND_PRIVATE_STAGE_LIMIT*days_between_reading
                    high_consumption = (daily_consumption-PUBLIC_AND_PRIVATE_STAGE_LIMIT)*(days_between_reading)

                    low_ect_tax = low_consumption*PUBLIC_AND_PRIVATE_LOW_SINGLE_TIME*RESIDENTIAL_ECT
                    high_ect_tax = high_consumption*PUBLIC_AND_PRIVATE_HIGH_SINGLE_TIME

                    low_vat_tax = (low_consumption*PUBLIC_AND_PRIVATE_LOW_SINGLE_TIME*(1+PUBLIC_AND_PRIVATE_ECT)+PUBLIC_AND_PRIVATE_DISTRIBUTION*low_consumption)*PUBLIC_AND_PRIVATE_VAT
                    high_vat_tax = (high_consumption*PUBLIC_AND_PRIVATE_HIGH_SINGLE_TIME*(1+PUBLIC_AND_PRIVATE_ECT)+PUBLIC_AND_PRIVATE_DISTRIBUTION*high_consumption)*PUBLIC_AND_PRIVATE_VAT

                    low_tariff_bill = (low_consumption*PUBLIC_AND_PRIVATE_LOW_SINGLE_TIME*(1+PUBLIC_AND_PRIVATE_ECT)+PUBLIC_AND_PRIVATE_DISTRIBUTION*low_consumption)*(1+PUBLIC_AND_PRIVATE_VAT)
                    bill = (high_consumption*PUBLIC_AND_PRIVATE_HIGH_SINGLE_TIME*(1+PUBLIC_AND_PRIVATE_ECT)+PUBLIC_AND_PRIVATE_DISTRIBUTION*high_consumption)*(1+PUBLIC_AND_PRIVATE_VAT)+low_tariff_bill
                    single_tariff_bill = bill

                    transferred_to_the_municipality = low_ect_tax + high_ect_tax
                    transferred_to_the_state = low_vat_tax + high_vat_tax
                      
                
            if multi_tariff:
                public_and_private_multi_tariff_count += 1
                bill = multi_tariff_bill
                transferred_to_the_municipality = public_and_private_multi*PUBLIC_AND_PRIVATE_ECT
                transferred_to_the_state = multi_tariff_bill/(1+PUBLIC_AND_PRIVATE_VAT)*PUBLIC_AND_PRIVATE_VAT
                
                
            public_and_private_consumer_count += 1
            public_and_private_usage_total += total_consumption
            

        if industry:
            consumer_type_code="Industry"
            industrial_consumer_count += 1
            industrial_usage_total += total_consumption
            single_tariff_bill=(total_consumption*INDUSTRY_SINGLE_TIME*(1+INDUSTRY_ECT)+INDUSTRY_DISTRIBUTION*total_consumption)*(1+INDUSTRY_VAT)
            multi_tariff_bill = (industry_multi*(1+INDUSTRY_ECT)+INDUSTRY_DISTRIBUTION*total_consumption)*(1+INDUSTRY_VAT)

            if total_consumption > 10000:
                exceeding_industry_consumer_count += 1

            if single_tariff:
                bill = single_tariff_bill
                transferred_to_the_municipality = total_consumption*INDUSTRY_SINGLE_TIME*INDUSTRY_ECT

            if multi_tariff:
                bill = multi_tariff_bill
                transferred_to_the_municipality = industry_multi*INDUSTRY_ECT

            if bill>100000:
                exceeding_industry_consumer_bill_count+=1

            transferred_to_the_state=bill/(1+INDUSTRY_VAT)*INDUSTRY_VAT



            
        if agricultural:
            consumer_type_code="Agricultural Activities"
            agricultural_consumer_count += 1
            agricultural_usage_total += total_consumption
            single_tariff_bill = (total_consumption*AGRICULTURAL_SINGLE_TIME*(1+AGRICULTURAL_ECT)+AGRICULTURAL_DISTRIBUTION*total_consumption)*(1+AGRICULTURAL_VAT)
            multi_tariff_bill = (agricultural_multi*(1+AGRICULTURAL_ECT)+AGRICULTURAL_DISTRIBUTION*total_consumption)*(1+AGRICULTURAL_VAT)
            if single_tariff:
                bill = single_tariff_bill
                transferred_to_the_municipality=total_consumption*AGRICULTURAL_SINGLE_TIME*AGRICULTURAL_ECT
            
            if multi_tariff:
                bill = multi_tariff_bill
                transferred_to_the_municipality = agricultural_multi*AGRICULTURAL_ECT


            transferred_to_the_state=bill/(1+AGRICULTURAL_VAT)*AGRICULTURAL_VAT

        if residential:
            consumer_type_code = "Residential"
            single_tariff_bill = (total_consumption*RESIDENTIAL_LOW_SINGLE_TIME*(1+RESIDENTIAL_ECT)+RESIDENTIAL_DISTRIBUTION*total_consumption)*(1+RESIDENTIAL_VAT)
            multi_tariff_bill = (residential_multi*(1+RESIDENTIAL_ECT)+RESIDENTIAL_DISTRIBUTION*total_consumption)*(1+RESIDENTIAL_VAT)
            if single_tariff:
                if daily_consumption <= RESIDENTIAL_STAGE_LIMIT:
                    bill = single_tariff_bill
                    transferred_to_the_municipality = total_consumption*RESIDENTIAL_LOW_SINGLE_TIME*RESIDENTIAL_ECT
                    transferred_to_the_state = single_tariff_bill*(1+RESIDENTIAL_VAT)*RESIDENTIAL_VAT
               
                if daily_consumption > RESIDENTIAL_STAGE_LIMIT:
                    low_consumption = RESIDENTIAL_STAGE_LIMIT*days_between_reading
                    high_consumption = (daily_consumption-RESIDENTIAL_STAGE_LIMIT)*(days_between_reading)

                    low_ect_tax = low_consumption*RESIDENTIAL_LOW_SINGLE_TIME*RESIDENTIAL_ECT
                    high_ect_tax = high_consumption*RESIDENTIAL_HIGH_SINGLE_TIME

                    low_vat_tax = (low_consumption*RESIDENTIAL_LOW_SINGLE_TIME*(1+RESIDENTIAL_ECT)+RESIDENTIAL_DISTRIBUTION*low_consumption)*RESIDENTIAL_VAT
                    high_vat_tax = (high_consumption*RESIDENTIAL_HIGH_SINGLE_TIME*(1+RESIDENTIAL_ECT)+RESIDENTIAL_DISTRIBUTION*high_consumption)*RESIDENTIAL_VAT

                    low_tariff_bill = (low_consumption*RESIDENTIAL_LOW_SINGLE_TIME*(1+RESIDENTIAL_ECT)+RESIDENTIAL_DISTRIBUTION*low_consumption)*(1+RESIDENTIAL_VAT)
                    bill = (high_consumption*RESIDENTIAL_HIGH_SINGLE_TIME*(1+RESIDENTIAL_ECT)+RESIDENTIAL_DISTRIBUTION*high_consumption)*(1+RESIDENTIAL_VAT)+low_tariff_bill
                    single_tariff_bill = bill

                    transferred_to_the_municipality = low_ect_tax + high_ect_tax
                    transferred_to_the_state = low_vat_tax + high_vat_tax
                    

            if multi_tariff:
                bill = multi_tariff_bill
                transferred_to_the_municipality = residential_multi*RESIDENTIAL_ECT
                transferred_to_the_state = multi_tariff_bill/(1+RESIDENTIAL_VAT)*RESIDENTIAL_VAT
                
            

    if lighting:
        consumer_type_code="Lighting"
        lighting_consumer_count += 1
        lighting_usage_total += total_consumption
        bill = (total_consumption*LIGHTING_SINGLE_TIME*(1+LIGHTING_ECT)+LIGHTING_DISTRIBUTION*total_consumption)*(1+LIGHTING_VAT)
        transferred_to_the_municipality=total_consumption*LIGHTING_SINGLE_TIME*LIGHTING_ECT
        transferred_to_the_state=bill/(1+LIGHTING_VAT)*LIGHTING_VAT

    if martyr_family == "Y" or martyr_family == "y":
        consumer_type_code="Residential (family of martyrs and veterans)"
        martyr_family_consumer_count += 1
        martyr_family_usage_total += total_consumption
        bill = (total_consumption*MARTYR_FAMILY_SINGLE_TIME*(1+MARTYR_FAMILY_ECT)+MARTYR_FAMILY_DISTRIBUTION*total_consumption)*(1+MARTYR_FAMILY_VAT)
        transferred_to_the_municipality=total_consumption*MARTYR_FAMILY_SINGLE_TIME*MARTYR_FAMILY_ECT
        transferred_to_the_state=bill/(1+MARTYR_FAMILY_VAT)*MARTYR_FAMILY_VAT


    
    if not residential:
        not_residential_count += 1
        if total_consumption >= not_residential_highest_usage:
            not_residential_highest_usage = total_consumption
            not_residential_highest_consumer_no = consumer_no
            not_residential_highest_consumer_type = consumer_type_code
            not_residential_highest_consumer_daily = total_consumption/days_between_reading
            not_residential_highest_usage_bill=bill/100

    
    transferred_to_the_municipality = transferred_to_the_municipality/100
    transferred_to_the_state = transferred_to_the_state/100
    total_tax = transferred_to_the_municipality + transferred_to_the_state
    bill = bill/100 #kr to tl
    consumption_fee = bill - total_tax

    print(f"consumer_no:{consumer_no}\n consumer_type_code:{consumer_type_code}\nday_consumption:{day_consumption}\n peak_consumption:{peak_consumption}\nnight_consumption:{night_consumption}\ntotal_consumption:{total_consumption}\n consumption_fee:{consumption_fee}\n transferred_to_the_municipality:{transferred_to_the_municipality}\n transferred_to_the_state:{transferred_to_the_state}\nbill:{bill}\nconsumption_yearly:{consumption_yearly}\nfree_consumer:{free_consumer}")


    if not lighting and (martyr_family == "N" or martyr_family == "n"):
        if multi_tariff_bill>single_tariff_bill and multi_tariff:
            profit_loss_situation="loss"
            who_made_a_loss_count+=1
            amount=(multi_tariff_bill-single_tariff_bill)/100
        elif multi_tariff_bill>single_tariff_bill and single_tariff:
            profit_loss_situation="profit"
            amount=(multi_tariff_bill-single_tariff_bill)/100
        elif single_tariff_bill>multi_tariff_bill and multi_tariff:
            profit_loss_situation="profit"
            amount=(single_tariff_bill-multi_tariff_bill)/100
        elif single_tariff_bill>multi_tariff_bill and single_tariff:
            profit_loss_situation="loss"
            who_made_a_loss_count+=1
            amount=(single_tariff_bill-multi_tariff_bill)/100
        elif single_tariff_bill==multi_tariff_bill and single_tariff:
            profit_loss_situation="not profit not loss"
            amount=(single_tariff_bill-multi_tariff_bill)/100
        elif single_tariff_bill==multi_tariff_bill and multi_tariff:
            profit_loss_situation="not profit not loss"
            amount=(single_tariff_bill-multi_tariff_bill)/100

        print(f"profit_loss_situation:{profit_loss_situation}, Profit/Loss amount according to other tariff {amount}")

    total_transferred_to_the_municipality+=transferred_to_the_municipality
    total_transferred_to_the_state+=transferred_to_the_state
    total_transferred_to_the_GDZ_corporation+=consumption_fee

    
    
total_consumer_count = industrial_consumer_count+public_and_private_consumer_count+agricultural_consumer_count+residential_consumer_count+lighting_consumer_count


if industrial_consumer_count != 0:
    industrial_consumer_perc = industrial_consumer_count/total_consumer_count*100
    avg_industrial_consumption = industrial_usage_total/industrial_consumer_count
    perc_exceeding_industrial_consumer = exceeding_industry_consumer_count/industrial_consumer_count*100
    perc_exceeding_industrial_consumer_bill=exceeding_industry_consumer_bill_count/industrial_consumer_count*100
    print(f"industrial_consumer_count:{industrial_consumer_count}\n industrial_consumer_perc:{industrial_consumer_perc}\n avg_industrial_consumption:{avg_industrial_consumption}\n industrial_usage_total:{industrial_usage_total}")
    print(f"exceeding_industry_consumer_count:{exceeding_industry_consumer_count}\n perc_exceeding_industrial_consumer:{perc_exceeding_industrial_consumer}\nexceeding_industry_consumer_bill_count:{exceeding_industry_consumer_bill_count}\nperc_exceeding_industrial_consumer_bill:{perc_exceeding_industrial_consumer_bill}")


if public_and_private_consumer_count != 0:
    public_and_private_consumer_perc = public_and_private_consumer_count/total_consumer_count*100
    avg_public_and_private_consumption = public_and_private_usage_total/public_and_private_consumer_count
    perc_public_and_private_single_tariff = public_and_private_single_tariff_count/public_and_private_consumer_count*100
    perc_public_and_private_multi_tariff = public_and_private_multi_tariff_count/public_and_private_consumer_count*100
    print(f"public_and_private_consumer_count:{public_and_private_consumer_count}\n public_and_private_consumer_perc:{public_and_private_consumer_perc}\n avg_public_and_private_consumption:{avg_public_and_private_consumption}\n public_and_private_usage_total:{public_and_private_usage_total}")
    print(f"public_and_private_single_tariff_count:{public_and_private_single_tariff_count}\n\
      public_and_private_multi_tariff_count:{public_and_private_multi_tariff_count}\n\
      perc_public_and_private_single_tariff:{perc_public_and_private_single_tariff}\n\
      perc_public_and_private_multi_tariff:{perc_public_and_private_multi_tariff}")


if agricultural_consumer_count != 0:
    agricultural_consumer_perc = agricultural_consumer_count/total_consumer_count*100
    avg_agricultural_consumption = agricultural_usage_total/agricultural_consumer_count
    print(f"agricultural_consumer_count:{agricultural_consumer_count}\n agricultural_consumer_perc:{agricultural_consumer_perc}\n avg_agricultural_consumption:{avg_agricultural_consumption}\n agricultural_usage_total:{agricultural_usage_total}")
if residential_consumer_count != 0:
    residential_consumer_perc = residential_consumer_count/total_consumer_count*100
    avg_residential_consumption = residential_usage_total/residential_consumer_count
    print(f"residential_consumer_count:{residential_consumer_count}\n residential_consumer_perc{residential_consumer_perc}\n avg_residential_consumption{avg_residential_consumption}\n residential_usage_total:{residential_usage_total}")
    print(f"highest_residential_consumer_no:{highest_residential_consumer_no}\n highest_residential_consumer_daily:{highest_residential_consumer_daily},bill:{bill}")


if lighting_consumer_count != 0:
    lighting_consumer_perc = lighting_consumer_count/total_consumer_count*100
    avg_lighting_consumption = lighting_usage_total/lighting_consumer_count
    print(f"lighting_consumer_count:{lighting_consumer_count}\n lighting_consumer_perc:{lighting_consumer_perc}\n avg_lighting_consumption:{avg_lighting_consumption}\n lighting_usage_total:{lighting_usage_total}")


bornova_total_consumption = industrial_usage_total+public_and_private_usage_total+agricultural_usage_total+residential_usage_total+lighting_usage_total






print(f"bornova_total_consumption:{bornova_total_consumption}")







if not_residential_count != 0:
    print(f"not_residential_highest_consumer_no:{not_residential_highest_consumer_no}\n\
        not_residential_highest_consumer_type:{not_residential_highest_consumer_type}\n\
        not_residential_highest_consumer_daily:{not_residential_highest_consumer_daily}\n\
        not_residential_highest_usage:{not_residential_highest_usage}\n\
        not_residential_highest_usage_bill:{not_residential_highest_usage_bill}")

print(f"total_transferred_to_the_GDZ_corporation:{total_transferred_to_the_GDZ_corporation}\ntotal_transferred_to_the_municipality:{total_transferred_to_the_municipality}\ntotal_transferred_to_the_state:{total_transferred_to_the_state}")

if not_martyr_family_and_not_lighting_multi != 0:
    print(f" the percentage of those who made a loss despite choosing multi-time tariff:{who_made_a_loss_count/not_martyr_family_and_not_lighting_multi*100}")
