file=open("web.txt","r")
year_pop_total=0
year_count=0
greatest_increase=-1
smallest_increase=10**5
b_pop=0
c_pop=0
for line in file:
    lin=line.split(":")
    year_pop_total+=int(lin[1])
    c_pop=lin[1]
    increase=int(c_pop)-int(b_pop)
    b_pop=c_pop
    year_count+=1
    if increase>=greatest_increase:
        greatest_increase=increase
    if increase<=smallest_increase:
        smallest_increase=increase

print(year_pop_total/year_count)
print(greatest_increase)
print(smallest_increase)


    
