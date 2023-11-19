A=int(input("A (longest) kenar uzunluğu:"))
B=int(input("B kenar uzunluğu:"))
C=int(input("C kenar uzunluğu:"))
a=A**2
b=B**2
c=C**2
if A>=B+C:
    print("üçgen değil.")
else:
    if a==b+c:
        print("right triangle")
    elif a<b+c:
        print("acute triangle")
    elif a>b+c:
        print("absute triangle")
