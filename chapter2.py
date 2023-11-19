bf=1
bf2=0
f=1
a=1
b=int(input("kaçıncı sayı:"))
while a<=b:
    f=bf+bf2
    bf2=bf
    bf=f
    
    a+=1
print(f)