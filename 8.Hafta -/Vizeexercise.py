a=int(input("a"))
b=int(input("b"))
c=int(input("c"))

if a>b and a<c:
    print(a)
elif a>c and a<b:
    print(a)
if c>b and c<a:
    print(c)
elif b>c and a<c:
    print(c)
if a>b and c<b:
    print(b)
elif c>b and a<b:
    print(b)