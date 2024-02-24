def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(a,a%b)
    
A=gcd(12,8)
print(A)

