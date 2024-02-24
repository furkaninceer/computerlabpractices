import math
fact=1
def factorial(j):
    global fact
    for i in range(1,j+1):
        fact*=i
    return fact

total=0
def f(x,y):
    global total
    for i in range(1,2*y,2):
        a=x**i/factorial(i)
        if i%4==1:
            total+=a
        elif i%4==3:
            total-=a
    print(total)
 

print(factorial(5))