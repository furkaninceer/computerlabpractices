x_min=-3
x_max=3
y_min=-3
y_max=3
total=0
no_result=0
count=0

for x in range(x_min,x_max+1):
    for y in range(y_min,y_max+1):
        count+=1
        if x+y!=0:
            
            value=(2*x+3*y-4*x*y+5)/(x+y)
            total+=value
            print(total)
        else:
            no_result+=1
            print("no_result")
print("avarage:",total/count-no_result)