
a=int(input("a:"))
while a>1:
    if a==2:
        print("prime")
    else:
        for i in range(2,int(a**0.5+1)):
            if a%i==0:
                print("not prime")
                break
    
        else:
            print("prime")
    a=int(input("a:(-1 to exit)"))
    

def prime(x):
    if x==2:
        return "prime"
    elif x>2:
        for i in range(2,int(x**0.5+1)):
            if x%i==0:
                return "not prime"
                break
        else:
            return "prime"
    

print(prime(4))