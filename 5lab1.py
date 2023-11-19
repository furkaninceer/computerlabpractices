import random
Min=1
Max=100
number=random.randint(Min,Max)
geuss=int(input("sayı tahmini:(1-100)"))
count=1
while number!=geuss:
    if number>geuss:
        print("UP")
    elif number<geuss:
        print("DOWN")
    count+=1
    geuss=int(input("sayı tahmini:"))
        

        
print("congruculations")
print(f"{count} kez denediniz")        
         
