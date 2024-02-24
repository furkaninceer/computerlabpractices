
def fib(num):
    if num==1 or num==2:
        return 1
    else:
        return fib(num-1)+fib(num-2)




num=int(input("num"))
f1=1
f2=1
while num>2:
    if num==1 or num==2:
        print(1)
    else:
        f3=f1+f2
        f1=f2
        f2=f3
        num-=1

print(f3)


    
    