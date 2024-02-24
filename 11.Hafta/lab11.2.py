def take_production(file,production_totals,day_counts):
    day_no=file.readline()
    while day_no!="":
        machine_no=int(file.readline())
        daily_production=int(file.readline())
        production_totals[machine_no-1]+=daily_production
        day_counts[machine_no-1]+=1
        day_no=file.readline()

def statistic(production_totals,day_counts,machine_count):
    print("Machine_No   Monthly_Production   Number Of Production Days   Daily Avarage")
    print("---------    ------------------   -------------------------   --------------")
    for i in range(int(machine_count)):
        print(f"{i+1:.10d}")
        print(f"{production_totals[i]:.18d}")
        print(f"{day_counts[i]:.25d}")
        print(production_totals[i]/day_counts[i])
        print(max(production_totals))
        max_production=max(production_totals)
        max_production_machine=production_totals.index(max_production)+1
        print(max_production)
def main():
    file=open("machines.txt","r")
    machine_count=file.readline()
    production_totals=0*machine_count
    day_counts=0*machine_count
    take_production(file,production_totals,day_counts)
    statistic(production_totals,day_counts,machine_count)
main()

