total=0

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
def f(x,y):
    global total
    for i in range(1,2*y,2):
        A=(x)**i/fact(i)
        if i%4==1:
            total+=A
        elif i%4==3:
            total-=A
    return total

print(f(2,3))
