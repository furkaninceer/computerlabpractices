ACCIDENT_CAUSE_COUNT=10

def get_accident_data_and_generate_lists(accident_file,all_provinces_accident_counts,all_provinces_damage_amount_totals):
    province_code_str=accident_file.readline()
    while province_code_str!="":
        province_code=int(province_code_str)
        accident_cause_code=int(accident_file.readline())
        damage_amount=int(accident_file.readline())
        all_provinces_accident_counts[province_code-1][accident_cause_code-1]+=1
        all_provinces_damage_amount_totals[province_code-1][accident_cause_code-1]+=damage_amount

        # update accident_counts and damage_amount_totals lists according to accident data read

        province_code_str=accident_file.readline()

def display_table(two_dimensional_list):
    accident_causes = ["Overspeed", "Rule Violation", "Carelessness", "Inc. Overtaking", "Insomnia",
                        "Awkwardness", "Alcohol", "Close Follow-up", "Aggressiveness", "Other"]
    print("Prov. Code ",end="")
    for accident_cause in accident_causes:
        print(f"{accident_cause:16}",end="")
    print("Total")
    print("---------- ",end="")
    for k in range(ACCIDENT_CAUSE_COUNT):
        print("--------------- ",end="")
    print("-----")
    # print the matrix and also the row and column totals of this matrix
    column_total=[0]*ACCIDENT_CAUSE_COUNT
    for province_code in range(81):
        print(f"{province_code+1:16}")
        for accident_cause_code in range(ACCIDENT_CAUSE_COUNT):
            print(f"{two_dimensional_list[province_code][accident_cause_code]:16}",end="")
            column_total[accident_cause_code]+=two_dimensional_list[province_code][accident_cause_code]
        print(f"{sum(two_dimensional_list[province_code])}")
    print("Total")
    for accident_cause_code in range(ACCIDENT_CAUSE_COUNT):
        print(column_total[accident_cause_code],end="")
        
    print(sum(column_total))
def main():
    try:
        accident_file=open("traffic_accidents.txt","r")
        # create 2 two-dimensional lists for the total number of accidents and total damage amounts by provinces and accident causes

        # call the corresponding function to get accident data from file and generate lists
        for i in range(81):
            all_provinces_accident_counts=[]
            all_provinces_damage_amount_totals=[]
            a_province_accident_counts=[0]*ACCIDENT_CAUSE_COUNT
            all_provinces_accident_counts.append(a_province_accident_counts)
            a_province_accident_counts_total=[0]*ACCIDENT_CAUSE_COUNT
            all_provinces_damage_amount_totals.append(a_province_accident_counts_total)
        accident_file.close()
    except IOError:
        print("Could not open or read data file!")
    else:
        print("Total Number of Accidents in a Year by Provinces and Causes of Accidents")
        # call the corresponding function to display the accident counts table

        any_key=input("press any key and enter to continue...")
        print("Total Damage Amounts in a Year by Provinces and Causes of Accidents")
        # call the corresponding function to display the damage amounts table


main()
